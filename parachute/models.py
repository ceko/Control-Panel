from django.db import models
from django.template.defaultfilters import slugify
from model_utils.managers import InheritanceManager

class Project(models.Model):    
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    lastedited = models.DateField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
class Step(models.Model):
    objects = InheritanceManager()
    
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    created = models.DateField(auto_now_add=True)
    lastedited = models.DateField(auto_now=True)
    priority = models.IntegerField()
    project = models.ForeignKey(Project)
    notes = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            
        super(Step, self).save(*args, **kwargs)
    
class SVNStep(Step):
    COMMAND_CHOICES = (
        ('export','export'),
        ('update','update'),
    )
    command = models.CharField(max_length=50, choices=COMMAND_CHOICES, default='update')
    source = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    
    def __unicode__(self):
        return '{0}:{1}'.format(self.name, self.command)
    
class ScriptStep(Step):
    script_location = models.CharField(max_length=255)
    
class FabricStep(Step):
    host = models.CharField(max_length=250)
    command_name = models.CharField(max_length=250)
    