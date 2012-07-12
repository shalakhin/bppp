#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'notes.views',
    url(r'^$', 'list_notes'),
    url(r'^my/$', 'list_my_notes'),
    url(r'^edit/(?P<id>\d+)/$', 'edit_note'),
    url(r'^remove/confirm/(?P<id>\d+)/$', 'remove_confirm'),
    url(r'^remove/(?P<id>\d+)/$', 'remove_note'),
    url(r'^(?P<id>\d+)', 'show_note'),
    url(r'^create/$', 'create_note'),
)
