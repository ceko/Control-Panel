from django.forms import ModelForm
import models

class ProjectForm(ModelForm):
    class Meta:
        model = models.Project 