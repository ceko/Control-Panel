
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('parachute.views',
    url(r'^$', 'default', name='deploystar_default'),
    url(r'^projects/add$', 'edit_project', name='add_project')
)