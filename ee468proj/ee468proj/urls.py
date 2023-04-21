#urls.py
from django.contrib import admin  
from django.urls import path, include

from ee468proj.views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('instructor/', instructor, name='instructor'),
    path('student/', student, name='student'),
    path('admin1/', admin1, name='admin1'),
    path('name/', name, name='name'),
    path('salary/', salary, name='name'),
    path('dept_name/', dept_name, name='dept_name'),
    path('minumumTable/', minumumTable, name='minumumTable'),
    path('maximumTable/', maximumTable, name='maximumTable'),
    path('averageTable/', averageTable, name='averageTable'),
    path('f6/', f6, name='f6'),
    ]