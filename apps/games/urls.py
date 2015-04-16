# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import GameListView


urlpatterns = patterns('',
    url(r'^games/$', name='game-list', view=GameListView.as_view()),
)
