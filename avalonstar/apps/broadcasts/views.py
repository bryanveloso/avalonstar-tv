# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from apps.games.models import Game

from .models import Broadcast, Highlight, Raid


class BroadcastDetailView(DetailView):
    model = Broadcast
    slug_field = 'number'


class BroadcastListView(ListView):
    model = Broadcast

    def get_context_data(self, **kwargs):
        context = super(BroadcastListView, self).get_context_data(**kwargs)
        context['first'] = Broadcast.objects.earliest()
        context['games'] = Game.objects.all()
        context['highlights'] = Highlight.objects.all()
        context['raids'] = Raid.objects.all()
        return context
