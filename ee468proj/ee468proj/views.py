# views.py
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import City
import mysql.connector





def showlist(request):
    results = City.objects.all
    return render(request, "home.html", {"showcity": results})


def salary(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        port='3307',
        passwd='Blackhorses1@',
        auth_plugin='mysql_native_password',
        database="university",
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
        host="localhost",
        user="root",
        port='3307',
        passwd='Blackhorses1@',
        auth_plugin='mysql_native_password',
        database="university",
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
        host="localhost",
        user="root",
        port='3307',
        passwd='Blackhorses1@',
        auth_plugin='mysql_native_password',
        database="university",
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
        host="localhost",
        user="root",
        port='3307',
        passwd='Blackhorses1@',
        auth_plugin='mysql_native_password',
        database="university",
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
        host="localhost",
        user="root",
        port='3307',
        passwd='Blackhorses1@',
        auth_plugin='mysql_native_password',
        database="university",
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
        host="localhost",
        user="root",
        port='3307',
        passwd='Blackhorses1@',
        auth_plugin='mysql_native_password',
        database="university",
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

