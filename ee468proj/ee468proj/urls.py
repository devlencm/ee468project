#urls.py
from django.contrib import admin  

from django.conf.urls import url
from django.urls import path, include

from ee468proj.views import salary, dept_name, showlist, minumumTable, maximumTable, averageTable, name


urlpatterns = [
    path('admin/', admin.site.urls),
    path('showlist/', showlist, name='showlist'),
    path('name/', name, name='name'),
    path('salary/', salary, name='name'),
    path('dept_name/', dept_name, name='dept_name'),
    path('minumumTable/', minumumTable, name='minumumTable'),
    path('maximumTable/', maximumTable, name='maximumTable'),
    path('averageTable/', averageTable, name='averageTable'),
    ]