#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

urlpatterns = patterns(
    'spaceship.views',
    url(r'^connect/$', login),
    url(r'^drop/$', 'logout_me'),
)
