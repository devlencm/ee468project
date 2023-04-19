# urls.py
from django.contrib import admin
import views
from django.urls import path, include

from ee468proj.views import minumumTable, maximumTable, averageTable

urlpatterns = [
    path('admin/', admin.site.urls),
    path('minumumTable/', minumumTable, name='minumumTable'),
    path('maximumTable/', maximumTable, name='maximumTable'),
    path('averageTable/', averageTable, name='averageTable'),
]