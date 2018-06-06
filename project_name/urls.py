""" Default urlconf for {{ project_name }} """

from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

#import {{ project_name}}.apps.main.urls

def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = [
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^', include({{ project_name }}.apps.main.urls)),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^bad/$', bad),
]

