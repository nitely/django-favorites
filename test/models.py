#-*- coding: utf-8 -*-

from django.db import models


class Article(models.Model):
    title = models.CharField("title", max_length=75)

    @property
    def display_name(self):
        return self.title

    def __unicode__(self):
        return self.title