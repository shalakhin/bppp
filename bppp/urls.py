#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from views import home_page

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', home_page),
    url(r'^notes/', include('notes.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^spaceship/', include('spaceship.urls')),
    url(r'^bppp/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)
