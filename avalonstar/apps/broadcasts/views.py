# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Broadcast


class BroadcastDetailView(DetailView):
    model = Broadcast
    slug_field = 'number'


class BroadcastListView(ListView):
    model = Broadcast
