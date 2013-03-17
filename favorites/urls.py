#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from views import FavoritesDetail


urlpatterns = patterns("favorites.views",
    url(r'^(?P<username>[\w.@+-]+)/$', FavoritesDetail.as_view(), name='favorites'),
    url(r'^action/create/$', 'favorite_create', name='favorite-create'),
    url(r'^action/delete/(?P<pk>\d+)/$', 'favorite_delete', name='favorite-delete'),
)