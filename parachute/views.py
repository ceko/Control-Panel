from django.shortcuts import render_to_response
from django.template import RequestContext
from annoying.decorators import render_to
import sys
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
    step_formset_manager = None
    
    if slug:
        #@todo: get project
        pass    
    if request.method == 'POST':
        new_step_form = step_form_removing = None
        project_form = None
        
        if 'add_step' in request.POST:            
            new_step_form = getattr(sys.modules['parachute.forms'], request.POST['new_step_type']+'Form')
            project_form = forms.ProjectForm(initial=dict(request.POST.items()))
        elif 'remove_step' in request.POST:            
            step_form_removing = getattr(sys.modules['parachute.forms'], request.POST['new_step_type']+'Form')
            project_form = forms.ProjectForm(initial=dict(request.POST.items()))
        elif 'add_project' in request.POST:
            project_form = forms.ProjectForm(request.POST)
            pass
        
        step_formset_manager = forms.StepFormFormsetManager(request, step_form_adding=new_step_form, step_form_removing=step_form_removing)
        
    else:
        project_form = forms.ProjectForm()
        step_formset_manager = forms.StepFormFormsetManager(request)
            
    return {
        'project_form' : project_form,
        'step_formset_manager' : step_formset_manager
    }
        