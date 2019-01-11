#!/usr/bin/env python
# coding=utf-8
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
