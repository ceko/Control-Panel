from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('dashboard.views',
    url(r'^$', 'default', name='dashboard_default')
)

urlpatterns += staticfiles_urlpatterns()