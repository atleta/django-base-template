
from django.conf.urls import url
from django.urls import include

from . import api

app_name = 'core'

urlpatterns = [
    url( '^api/v1/', include(api.urls))
]
