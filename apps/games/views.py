# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Game


class GameListView(ListView):
    model = Game
