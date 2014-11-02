# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetalView, TemplateView

from .models import Broadcast


class BroadcastList(ListView):
    model = Broadcast
