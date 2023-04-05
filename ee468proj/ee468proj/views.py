# views.py
from django.shortcuts import render
from myapp.models import City


def showlist(request):
    results = City.objects.all
    return render(request, "home.html", {"showcity": results})