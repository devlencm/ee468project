# views.py
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import City
import mysql.connector

def showlist(request):
    results = City.objects.all
    return render(request, "home.html", {"showcity": results})


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

    table_data = '<table style="width:400px">'
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

    table_data = '<table style="width:400px">'
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

    table_data = '<table style="width:400px">'
    for (dept_name, min_salary) in mycursor:
        row = '<tr><td>{}</td><td>{}</td></tr>'.format(dept_name, min_salary)
        table_data += row
    table_data += '</table>'

    mycursor.close()
    mydb.close()
    context = {'table_data': table_data}
    return render(request, 'table.html', context)

