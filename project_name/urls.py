""" Default urlconf for {{ project_name }} """

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views import static

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

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static.serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
