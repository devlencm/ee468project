# views.py

import mysql.connector
from django.shortcuts import render
from .models import Instructor


def home(request):
    return render(request, "homepage.html")

def admin1(request):
    return render(request, "home.html")

def admin2(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        year = request.POST.get('year', '')
        semester = request.POST.get('semester', '')
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
            query3 = 'select sum(amount) from investigator as v join grantaward as g on v.award_id = g.award_id and v.agent = g.agent join instructor on id = teacher_id where name = %s and ((startYear = %s and startMonth <= 6) or (startYear >= %s and endYear>= %s) or (endYear = %s and endMonth <= 6));'
        else:
            query3 = 'select sum(amount) from investigator as v join grantaward as g on v.award_id = g.award_id and v.agent = g.agent join instructor on id = teacher_id where name = %s and ((startYear = %s and startMonth <= 12) or (startYear >= %s and endYear>= %s) or (endYear = %s and endMonth > 8));'

        if semester == 2:
            query4 = 'select count(title) from publication join instructor on id = teacher_id where name = %s and ((year = %s and month < 6) or (year > %s));'
        else:
            query4 = 'select count(title) from publication join instructor on id = teacher_id where name = %s and ((year = %s and month <= 12) or (year > %s));'

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
        table_data += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(name, result1, result2, result3, result4)
        table_data += '</table>'

        mycursor.close()
        mydb.close()
        context = {'table_data': table_data}
        return render(request, 'f3.html', context)

    else:
        names = Instructor.objects.values('name')

        context = {'names': names}
        return render(request, 'base.html', context)


def instructor(request):
    return render(request, "instructor.html")

def student(request):
    return render(request, "student.html")
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


