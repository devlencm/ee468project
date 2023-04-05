from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. \nAgain")

def students(request):
    return HttpResponse("Hello students. \nAgain")

def instructors(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='password',
    auth_plugin='mysql_native_password',
    database="university",
    )

    mycursor = mydb.cursor()

    mycursor.execute('select * from instructor where salary>90000')

    data='<table style="width:400px">'
    for (id, name, dept, salary) in mycursor:
        r= ('<tr>'+ \
            '<th>'+str(id)+'</th>'+\
            '<th>'+name+'</th>'+\
            '<th>'+dept+'</th>'+\
            '<th>'+str(salary)+'</th>'+\
            '</tr>')
        data += r
    data +='</table>'

    mycursor.close()
    mydb.close()

    return HttpResponse("Hello, world. You're at the polls index.\n"+data)