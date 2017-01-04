""" Default urlconf for {{ project_name }} """

from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()

#import {{ project_name}}.apps.main.urls

def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include({{ project_name }}.apps.main.urls)),
    url(r'^bad/$', bad),
)

