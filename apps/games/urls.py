# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import GameListView


urlpatterns = [
    url(r'^games/$', name='game-list', view=GameListView.as_view()),
]
