# views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Department
from .models import Section

import mysql.connector
def home(request):
    return render(request, "homepage.html")

def admin1(request):
    return render(request, "home.html")

def instructor(request):
    return render(request, "instructor.html")

def student(request):
    depts = Department.objects.all()
    years = Section.objects.values('year').distinct()
    semesters = Section.objects.values('semester').distinct()
    context = {'depts' : depts,
               'years' : years,
               'semesters' : semesters
               }
    return render(request, "student.html", context)
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