#urls.py
from django.contrib import admin  
from django.urls import path, include

from ee468proj.views import salary, dept_name, admin1, minumumTable, maximumTable, averageTable, name, home, instructor, student


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
    ]