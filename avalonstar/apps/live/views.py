# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from apps.broadcasts.models import Broadcast


class AwayView(TemplateView):
    template_name = 'live/away.html'


class BumperView(TemplateView):
    template_name = 'live/bumper.html'

    def get_context_data(self, **kwargs):
        context = super(BumperView, self).get_context_data(**kwargs)
        context['broadcast'] = Broadcast.objects.latest()
        return context


class GameView(TemplateView):
    template_name = 'live/game.html'


class PrologueView(TemplateView):
    template_name = 'live/prologue.html'

    def get_context_data(self, **kwargs):
        context = super(PrologueView, self).get_context_data(**kwargs)
        context['broadcast'] = Broadcast.objects.latest()
        return context
