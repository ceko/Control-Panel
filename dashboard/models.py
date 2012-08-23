from django.db import models
from utilities.shortcuts import django_meta

class Log(models.Model):
    
    #fields
    date_logged = models.DateField(auto_now_add=True)    
    LEVEL_CHOICES = (
        ('DEBUG','DEBUG'),
        ('INFO','INFO'),
        ('WARN','WARN'),
        ('ERROR','ERROR'),
        ('FATAL','FATAL')        
    )
    level = models.CharField(max_length=5, choices=LEVEL_CHOICES) 
    app = models.CharField(max_length=150)
    message = models.TextField()
        
    #options
    ordering = ['-date_logged']    
        
    @staticmethod
    def get_recent(max):
        return Log.objects.all()[:max]
    
class LogWebView(object):
            
    @staticmethod
    @django_meta(Log)        
    def get_displayed_fields():            
        return [
            'date_logged',
            'level',
            'app',
            'message'
        ]