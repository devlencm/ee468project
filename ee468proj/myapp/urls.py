from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index),
    path('students/', views.students),
    path('instructors/', views.instructors),
    path('admin/', admin.site.urls),
]