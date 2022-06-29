from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()

    return render(request, 'projects.html', {'projects' : projects})