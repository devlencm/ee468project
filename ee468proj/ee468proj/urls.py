#urls.py
from django.contrib import admin  
from django.urls import path, include

from ee468proj.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('instructor/', instructor, name='instructor'),
    path('instructor2/', instructor2, name='instructor2'),
    path('student/', student, name='student'),
    path('admin1/', admin2, name='admin2'),
    path('feature5/',feature5, name='feature5'),
    path('f6', f6, name='f6'),
    path('name/', name, name='name'),
    path('salary/', salary, name='name'),
    path('dept_name/', dept_name, name='dept_name'),
    path('minumumTable/', minumumTable, name='minumumTable'),
    path('maximumTable/', maximumTable, name='maximumTable'),
    path('averageTable/', averageTable, name='averageTable'),
    path('instrr/', instrr, name='instrr'),
    path('instr/', instr, name='instr'),

    ]