#-*- coding: utf-8 -*-

import datetime

from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """note"""
    public = models.BooleanField(
        verbose_name=u"Публично доступная записка",
        default=False)
    on_top = models.BooleanField(
        verbose_name=u"Показывать выше остальных записок", default=False)
    name = models.CharField(verbose_name=u"Название записки", max_length=100)
    content = models.TextField(verbose_name=u"Текст записки")
    author = models.ForeignKey(User)
    pubdate = models.DateTimeField(
        verbose_name="Дата создания", default=datetime.datetime.now)

    class Meta:
        ordering = ['-pubdate']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/notes/%s' % self.id
