from controlpanel.plugins import get_plugin_settings

def cpanel_plugins(request):
    cpanel_plugins = get_plugin_settings()
    selected_plugin = None
    for p in cpanel_plugins:        
        if request.path.startswith('/'+p.DEFAULT_URL):            
            selected_plugin = p
            break
    
    return {
        'cpanel_plugins' : cpanel_plugins,
        'selected_plugin' : selected_plugin     
    }
