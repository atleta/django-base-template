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

SITE_HEADER = 'WebAssess <span style="background: {bgcolor}; color: {color}">{deployment}</span> [revision {version} @ {timestamp}]'.format(
    bgcolor=settings.ADMIN_LABEL_BACKGROUND,
    color=settings.ADMIN_LABEL_COLOR,
    deployment=settings.DEPLOYMENT_NAME,
    version=settings.VERSION,
    timestamp=settings.VERSION_TIMESTAMP.isoformat()
)

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


