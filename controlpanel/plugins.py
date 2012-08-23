import sys
from threading import Lock
import controlpanel.settings as settings

plugins = []
def get_plugin_settings():
    lock = Lock()
    lock.acquire()
    try:
        if len(plugins) > 0:
            return plugins
        
        for plugin in settings.CPANEL_APPS:
            plugins.append(CpanelPluginSettings(plugin))
    finally:
        lock.release()
        
    return plugins

class CpanelPluginSettings(object):
    
    @property
    def relative_path(self):
        return self._relative_path
    
    def __init__(self, plugin_relative_path):
        self._relative_path = plugin_relative_path   
                    
        settings_path = '{0}.settings'.format(plugin_relative_path)        
        __import__(settings_path)
        self._settings = sys.modules[settings_path]
        
    def __getattribute__(self, name):        
        try:                
            return object.__getattribute__(self,'_settings').__getattribute__(name)        
        except AttributeError:
            return object.__getattribute__(self, name)
