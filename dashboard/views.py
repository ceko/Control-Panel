from django.shortcuts import render_to_response
from django.template import RequestContext
from annoying.decorators import render_to
import models
from utilities.viewhelpers import DataSet

@render_to('dashboard/default.html')
def default(request):    
    return {
        'recent_log_entries' : DataSet.from_model_query(models.Log.get_recent(10), (models.LogWebView.get_displayed_fields()))
    }
