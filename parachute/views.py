from django.shortcuts import render_to_response
from django.template import RequestContext
from annoying.decorators import render_to
import models
import forms

@render_to('parachute/default.html')
def default(request):
    projects = models.Project.objects.all()
       
    return {
        'projects' : projects
    }

@render_to('parachute/edit_project.html')
def edit_project(request, slug=None):
    project = None
    project_form = None
    
    if slug:
        #@todo: get project
        pass    
    if request.method == 'POST':
        pass
    else:
        project_form = forms.ProjectForm()
            
    return {
        'project_form' : project_form 
    }
        