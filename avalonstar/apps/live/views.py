# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from apps.broadcasts.models import Broadcast


class BroadcastContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BroadcastContextMixin, self).get_context_data(**kwargs)
        context['broadcast'] = Broadcast.objects.latest()
        return context


class AwayView(BroadcastContextMixin, TemplateView):
    template_name = 'live/away.html'


class BumperView(BroadcastContextMixin, TemplateView):
    template_name = 'live/bumper.html'


class DiscussionView(BroadcastContextMixin, TemplateView):
    template_name = 'live/discussion.html'


class GameView(TemplateView):
    template_name = 'live/game.html'


class PrologueView(BroadcastContextMixin, TemplateView):
    template_name = 'live/prologue.html'
