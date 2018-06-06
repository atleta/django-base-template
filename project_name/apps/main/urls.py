
from django.conf.urls import url
from django.urls import include

from . import api

urlpatterns = [
    url( '^api/v1/', include(api.urls))
]
