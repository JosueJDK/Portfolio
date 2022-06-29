from django.shortcuts import render
from django.http import Http404
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()

    return render(request, 'projects.html', {'projects' : projects})

def project_details(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
        return render(request, 'project_details.html', {'project' : project})
        
    except Project.DoesNotExist:
        raise Http404("No MyModel matches the given query. Error: 404")