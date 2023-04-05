# urls.py
from django.contrib import admin
from myapp import views
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showlist/', views.showlist, name='showlist'),
]