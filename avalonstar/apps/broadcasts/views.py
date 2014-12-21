# -*- coding: utf-8 -*-
from __future__ import division

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from apps.games.models import Game

from .models import Broadcast, Highlight, Raid


class BroadcastDetailView(DetailView):
    model = Broadcast
    slug_field = 'number'


class BroadcastListView(ListView):
    model = Broadcast

    def calculate_highlights_per_episode(self, **kwargs):
        episodes = Broadcast.objects.count()
        highlights = Highlight.objects.count()
        return round((highlights / episodes), 2)

    def calculate_raids_per_episode(self, **kwargs):
        episodes = Broadcast.objects.count()
        raids = Raid.objects.count()
        return round((raids / episodes), 2)

    def get_context_data(self, **kwargs):
        context = super(BroadcastListView, self).get_context_data(**kwargs)
        context['first'] = Broadcast.objects.earliest()
        context['games'] = Game.objects.all()
        context['games_completed'] = Game.objects.filter(is_completed=True)

        # Highlights.
        context['highlights'] = Highlight.objects.all()
        context['highlights_per_episode'] = self.calculate_highlights_per_episode()

        # Raids.
        context['raids'] = Raid.objects.all()
        context['raids_per_episode'] = self.calculate_raids_per_episode()
        return context
