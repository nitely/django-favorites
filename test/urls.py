#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from views import SingleArticle

urlpatterns = patterns("",
    url(r'^(?P<pk>\d+)/$', SingleArticle.as_view()),
)