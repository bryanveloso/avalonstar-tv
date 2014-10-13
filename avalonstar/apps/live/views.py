# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class AwayView(TemplateView):
    template_name = 'live/away.html'


class BumperView(TemplateView):
    template_name = 'live/bumper.html'


class GameView(TemplateView):
    template_name = 'live/game.html'


class PrologueView(TemplateView):
    template_name = 'live/prologue.view'
