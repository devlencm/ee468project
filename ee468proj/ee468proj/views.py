# views.py
from django.http import HttpResponse
from django.shortcuts import render
import flask
import mysql.connector


def home(request):
    return render(request, "homepage.html")

def admin1(request):
    return render(request, "home.html")

def instructor(request):
    return render(request, "instructor.html")

def student(request):
    return render(request, "student.html")

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/feature5', methods=['GET', 'POST'])
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
    #course = request.Post['course']
   # instructor = request.Post['instructorname']
   # semester = request.Post['semester']
    q = 'SELECT s.name FROM takes as t JOIN Student as s ON t.student_id = s.student_id JOIN section as sec ON t.course_id = sec.course_id AND t.sec_id = sec.sec_id AND t.semester = sec.semester AND t.year = sec.year JOIN teaches as tch ON sec.course_id = tch.course_id AND sec.sec_id = tch.sec_id AND sec.semester = tch.semester AND sec.year = tch.year JOIN instructor as inst ON tch.teacher_id = inst.id WHERE t.semester = 1 AND inst.name = "Hou" AND t.course_id = "EE468";'

    mycursor.execute(q)

    table_data = '<table style="width:400px"><th>Name</th></tr>'
    for (name) in mycursor:
        name1 = str(name[0])
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

