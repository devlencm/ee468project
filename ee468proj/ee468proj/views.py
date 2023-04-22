# views.py
from django.http import HttpResponse
from django.shortcuts import render
from flask import Flask, request
from django.views.decorators.csrf import csrf_protect
import mysql.connector
from .models import *


def admin2(request):
    name = request.POST.get('name', '')
    year = request.POST.get('year', '')
    semester = request.POST.get('semester', '')
    names = Instructor.objects.all()
    years = Takes.objects.values('year').distinct
    semesters = Takes.objects.values('semester').distinct

    mydb = mysql.connector.connect(
        host="128.153.13.175",
        port="3306",
        user="group_c",
        passwd='ChaBraKatMik',
        auth_plugin='mysql_native_password',
        database="university_group_c",
    )
    mycursor = mydb.cursor()
    query1 = 'select count(sec_id) from instructor join teaches on teaches.teacher_id = instructor.id where name = ' \
             '%s and year = %s and semester = %s;'
    query2 = 'select count(distinct(student_id)) as "#Students" from instructor join teaches on teaches.teacher_id ' \
             '= instructor.id right join takes on takes.course_id = teaches.course_id ' \
             'where name = %s and takes.year = %s and takes.semester = %s group by takes.semester, takes.year;'
    if (semester == 2):
        query3 = 'select sum(amount) from investigator as v join grantaward as g on v.award_id = g.award_id and v.agent ' \
                 '= g.agent join instructor on id = teacher_id where name = %s and ((startYear = %s and startMonth <= 6)' \
                 ' or (startYear >= %s and endYear>= %s) or (endYear = %s and endMonth <= 6));'
    else:
        query3 = 'select sum(amount) from investigator as v join grantaward as g on v.award_id = g.award_id and v.agent ' \
                 '= g.agent join instructor on id = teacher_id where name = %s and ((startYear = %s and startMonth <= 12)' \
                 ' or (startYear >= %s and endYear>= %s) or (endYear = %s and endMonth > 8));'

    if semester == 2:
        query4 = 'select count(title) from publication join instructor on id = teacher_id where name = %s and ((year = ' \
                 '%s and month < 6) or (year > %s));'
    else:
        query4 = 'select count(title) from publication join instructor on id = teacher_id where name = %s and ((year = ' \
                 '%s and month <= 12) or (year > %s));'

    mycursor.execute(query1, (name, year, semester))
    result1 = mycursor.fetchone()[0]

    mycursor.execute(query2, (name, year, semester))
    row = mycursor.fetchone()
    if row is None:
        result2 = 0
    else:
        result2 = row[0]

    mycursor.execute(query3, (name, year, year, year, year))
    result3 = mycursor.fetchone()[0]

    mycursor.execute(query4, (name, year, year))
    result4 = mycursor.fetchone()[0]

    table_data = '<table style="width:600px"><tr><th>Name</th><th>#Sections</th><th>#Students</th><th>Funding</th><th>Papers Published</th></tr>'
    table_data += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(name, result1, result2,
                                                                                            result3, result4)
    table_data += '</table>'

    mycursor.close()
    mydb.close()
    if request.method == 'POST':
        context = {'table_data': table_data, 'names': names, 'years': years, 'semesters': semesters}
        return render(request, 'f3.html', context)
    else:
        context = {'names': names, 'years': years, 'semesters': semesters}
        return render(request, 'base.html', context)


def home(request):
    return render(request, "homepage.html")

def admin1(request):
    return render(request, "home.html")

def instructor(request):
    return render(request, "instructor.html")

def instructor2(request):
    return render(request, "instructor2.html")

def student(request):
    depts = Department.objects.all()
    years = Section.objects.values('year').distinct()
    semesters = Section.objects.values('semester').distinct()
    context = {'depts' : depts,
               'years' : years,
               'semesters' : semesters
               }
    return render(request, "student.html", context)

def f6(request):
    dept = request.POST.get('dept', 0)
    year = request.POST.get('year', 0)
    semester = request.POST.get('sem', 0)

    mydb = mysql.connector.connect(
    host="128.153.13.175",
    port="3306",
    user="group_c",
    passwd='ChaBraKatMik',
    auth_plugin='mysql_native_password',
    database="university_group_c",
    )

    mycursor = mydb.cursor()

    query = "select s.course_id, s.sec_id, s.semester, s.year, s.building, s.room, s.capacity from section s join " \
            "course c on s.course_id = c.course_id where c.dept_name = '" + dept + "' and s.semester = " + semester + \
            " and s.year = " + year + ";"
    mycursor.execute(query)

    table_data = '<table style="width:75%"><th>Course</th><th>Section</th><th>Semester</th><th>Year</th>' \
                 '<th>Building</th><th>Room</th><th>Capacity</th></tr>'
    if mycursor:
        for (course_id, sec_id, semester, year, building, room, capacity) in mycursor:
            row = '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format\
                (course_id, sec_id, semester, year, building, room, capacity)
            table_data += row
        table_data += '</table>'
    else:
        table_data = '<p>No results found.</p>'
    mycursor.close()
    mydb.close()
    context = {'table_data': table_data}
    return render(request, 'f6.html', context)

def feature5(request):
    mydb = mysql.connector.connect(
        host="128.153.13.175",
        port="3306",
        user="group_c",
        passwd='ChaBraKatMik',
        auth_plugin='mysql_native_password',
        database="university_group_c",
    )
    mycursor = mydb.cursor()

    print(request.GET)
    instructor = request.POST.get('instructor')
    course = request.POST.get('course1')
    semester = request.POST.get('semester')


    q = 'SELECT s.name FROM takes as t JOIN Student as s ON t.student_id = s.student_id JOIN section as sec ON ' \
            't.course_id = sec.course_id AND t.sec_id = sec.sec_id AND t.semester = sec.semester AND t.year = sec.year ' \
         'JOIN teaches as tch ON sec.course_id = tch.course_id AND sec.sec_id = tch.sec_id AND sec.semester = tch.semester ' \
         'AND sec.year = tch.year JOIN instructor as inst ON tch.teacher_id = inst.id WHERE t.semester = %s AND ' \
         'inst.name = %s AND t.course_id = %s;'

    mycursor.execute(q, (semester, instructor, course))

    if(course == 1):
        sem = "Spring"
    else:
        sem = "Fall"

    table_data = f'<table style="width:400px"><th>Students [{instructor}, {course}, {sem}]</th></tr>'
    for (name) in mycursor:
        name1= str(name[0])
        row = '<tr><td>{}</td></tr>'.format(name1)
        table_data += row
    table_data += '</table>'

    mycursor.close()
    mydb.close()
    context = {'table_data': table_data}
    return render(request, 'f5.html', context)
def salary(request):
    mydb = mysql.connector.connect(
        host="128.153.13.175",
        port="3306",
        user="group_c",
        passwd='ChaBraKatMik',
        auth_plugin='mysql_native_password',
        database="university_group_c",
    )
    mycursor = mydb.cursor()
    mycursor.execute('select name from instructor order by salary asc;')

    table_data = '<table style="width:400px"><th>Name</th></tr>'
    for (name) in mycursor:
        row = '<tr><td>{}</td></tr>'.format(name)
        table_data += row
    table_data += '</table>'

    mycursor.close()
    mydb.close()
    context = {'table_data': table_data}
    return render(request, 'dept_name.html', context)
def dept_name(request):
    mydb = mysql.connector.connect(
        host="128.153.13.175",
        port="3306",
        user="group_c",
        passwd='ChaBraKatMik',
        auth_plugin='mysql_native_password',
        database="university_group_c",
    )

    mycursor = mydb.cursor()

    mycursor.execute('Select name from instructor order by dept_name asc;')

    table_data = '<table style="width:400px"><th>Name</th></tr>'
    for (name) in mycursor:
        row = '<tr><td>{}</td></tr>'.format(name)
        table_data += row
    table_data += '</table>'

    mycursor.close()
    mydb.close()
    context = {'table_data': table_data}
    return render(request, 'dept_name.html', context)
def name(request):
    mydb = mysql.connector.connect(
        host="128.153.13.175",
        port="3306",
        user="group_c",
        passwd='ChaBraKatMik',
        auth_plugin='mysql_native_password',
        database="university_group_c",
    )

    mycursor = mydb.cursor()

    mycursor.execute('Select name from instructor order by name asc;')

    table_data = '<table style="width:400px"><th>Name</th></tr>'
    for (name) in mycursor:
        row = '<tr><td>{}</td></tr>'.format(name)
        table_data += row
    table_data += '</table>'

    mycursor.close()
    mydb.close()
    context = {'table_data': table_data}
    return render(request, 'name.html', context)
def minumumTable(request):
    mydb = mysql.connector.connect(
    host="128.153.13.175",
    port="3306",
    user="group_c",
    passwd='ChaBraKatMik',
    auth_plugin='mysql_native_password',
    database="university_group_c",
    )

    mycursor = mydb.cursor()

    mycursor.execute('select dept_name, min(salary) as min from instructor where salary is not null group by dept_name;')

    table_data = '<table style="width:400px"><th>Department Name</th><th>Minimum Salary</th></tr>'
    for (dept_name, min_salary) in mycursor:
        row = '<tr><td>{}</td><td>{}</td></tr>'.format(dept_name, min_salary)
        table_data += row
    table_data += '</table>'

    mycursor.close()
    mydb.close()
    context = {'table_data': table_data}
    return render(request, 'min_table.html', context)

def maximumTable(request):
    mydb = mysql.connector.connect(
    host="128.153.13.175",
    port="3306",
    user="group_c",
    passwd='ChaBraKatMik',
    auth_plugin='mysql_native_password',
    database="university_group_c",
    )


    mycursor = mydb.cursor()

    mycursor.execute('select dept_name, max(salary) as max from instructor where salary is not null group by dept_name;')

    table_data = '<table style="width:400px"><tr><th>Department Name</th><th>Maximum Salary</th></tr>'
    for (dept_name, min_salary) in mycursor:
        row = '<tr><td>{}</td><td>{}</td></tr>'.format(dept_name, min_salary)
        table_data += row
    table_data += '</table>'

    mycursor.close()
    mydb.close()
    context = {'table_data': table_data}
    return render(request, 'max_table.html', context)


def averageTable(request):
    mydb = mysql.connector.connect(
    host="128.153.13.175",
    port="3306",
    user="group_c",
    passwd='ChaBraKatMik',
    auth_plugin='mysql_native_password',
    database="university_group_c",
    )

    mycursor = mydb.cursor()

    mycursor.execute('select dept_name, avg(salary) as avg from instructor where salary is not null group by dept_name;')

    table_data = '<table style="width:400px"><th>Department Name</th><th>Average Salary</th></tr>'
    for (dept_name, min_salary) in mycursor:
        row = '<tr><td>{}</td><td>{}</td></tr>'.format(dept_name, min_salary)
        table_data += row
    table_data += '</table>'

    mycursor.close()
    mydb.close()
    context = {'table_data': table_data}
    return render(request, 'table.html', context)
    
def instr(request):
    if request.method == 'POST' and 'submit' in request.POST:
        name = request.POST['name']
        year = request.POST['year']
        semester = request.POST['semester']
    
        mydb = mysql.connector.connect(
        host="128.153.13.175",
        port="3306",
        user="group_c",
        passwd='ChaBraKatMik',
        auth_plugin='mysql_native_password',
        database="university_group_c",
        )

        mycursor = mydb.cursor()
        query = 'select course_id, sec_id, numStus from teaches left join (select course_id as course, sec_id as sec, semester as sem, year as yr, count(student_id) as numStus from takes group by course, sec, sem, yr) as t2 on course_id = t2.course and sec_id = t2.sec and semester = t2.sem and year = t2.yr where semester = ' + semester + ' and year = ' + year + ' and teacher_id = ' + name + ';'

        mycursor.execute(query)
    
        if mycursor:
            table_data = '<table style="width:400px"><th>Course ID</th><th>Section</th><th>Number of Students</th></tr>'
            for (course_id, sec_id, numStus) in mycursor:
                row = '<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(course_id, sec_id, numStus)
                table_data += row
            table_data += '</table>'
        else:
            table_data = '<p>No results found.</p>'

        mycursor.close()
        mydb.close()
        context = {'table_data': table_data}
        return render(request, 'instr.html', context)

def instrr(request):
    return render(request, "instrr.html")