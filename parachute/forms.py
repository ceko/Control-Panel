from django import forms
import sys
import models
import utilities.reflection
from django.forms.formsets import formset_factory

class ProjectForm(forms.ModelForm):
        
    new_step_type = forms.ChoiceField(
        choices = ((x.__name__, x.__name__) for x in utilities.reflection.inheritors(models.Step)),
        required = False 
    )
    
    def disable_validation(self):
        super(ProjectForm, self).clean()        
        self._errors.clear()        
            
    class Meta:
        model = models.Project 
        
class StepForm(forms.ModelForm):
    
    class Meta:
        model = models.Step
        
class SVNStepForm(forms.ModelForm):
    
    class Meta:
        model = models.SVNStep        
        
class ScriptStepForm(forms.ModelForm):

    class Meta:
        model = models.ScriptStep

class FabricStepForm(forms.ModelForm):
    
    def default_template(self):
        return 'parachute/forms/edit_fabric_step_form.html'
    
    class Meta:
        model = models.FabricStep
        
class StepFormFormsetManager(object):
    
    def __init__(self, request, step_form_adding = None, step_form_removing = None):        
        if request.method == 'POST':       
            step_form = step_form_adding or step_form_removing
            form_delta = 1 if step_form_adding else -1
            post_data = request.POST.copy()                       
            self.formsets = []
            for form in self._get_step_model_forms():
                if form == step_form:
                    post_data[step_form.__name__ + '-TOTAL_FORMS'] = int(post_data[step_form.__name__ + '-TOTAL_FORMS']) + form_delta 
                    
                formset = formset_factory(form)
                f = formset(post_data, request.FILES, prefix=form.__name__)
                self.formsets.append(f)
        else:   
            self.formsets = []
            for form in self._get_step_model_forms():
                formset = formset_factory(form, extra=0)
                self.formsets.append(formset(prefix=form.__name__))
        
        self.request = request
    
    def _get_step_model_forms(self):
        return (getattr(sys.modules[__name__], x.__name__+'Form') for x in utilities.reflection.inheritors(models.Step))
    
    def add_empty_form(self, klass):             
        for formset in self.formsets:
            if formset.form == klass:
                formset.extra = 1
                return
        
    def get_forms(self):        
        forms = []        
        for formset in self.formsets:
            forms += formset.forms
            
        return forms
    
    def get_management_forms(self):
        management_forms = []        
        for formset in self.formsets:
            management_forms += formset.management_form
            
        return management_forms        
    