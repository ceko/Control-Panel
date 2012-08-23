from django.conf.urls import patterns, include, url
from controlpanel.plugins import get_plugin_settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',       
    # Examples:
    # url(r'^$', 'controlpanel.views.home', name='home'),
    # url(r'^controlpanel/', include('controlpanel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

for plugin in get_plugin_settings():    
    urlpatterns.append(url(r'^{0}'.format(plugin.DEFAULT_URL), include('{0}.urls'.format(plugin.PLUGIN_NAME))))
    
urlpatterns += staticfiles_urlpatterns()
urlpatterns.append(url(r'admin/', include(admin.site.urls)))