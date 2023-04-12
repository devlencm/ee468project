#urls.py
from django.contrib import admin  
from django.urls import path, include

from ee468proj.views import showlist, minumumTable, maximumTable, averageTable


urlpatterns = [
    path('admin/', admin.site.urls),
    path('showlist/', showlist, name='showlist'),
    path('minumumTable/', minumumTable, name='minumumTable'),
    path('maximumTable/', maximumTable, name='maximumTable'),
    path('averageTable/', averageTable, name='averageTable'),
    ]