# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, View

from braces.views import JSONResponseMixin

from apps.broadcasts.models import Broadcast
from apps.live.models import Message
from apps.subscribers.models import Ticket

from .utils import fetch_stream, is_episodic


class BroadcastContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BroadcastContextMixin, self).get_context_data(**kwargs)
        context['broadcast'] = Broadcast.objects.latest()
        context['message_list'] = Message.objects.order_by('?')
        context['ticket'] = Ticket.objects.latest()
        return context


class AwayView(BroadcastContextMixin, TemplateView):
    template_name = 'live/away.html'


class DiscussionView(BroadcastContextMixin, TemplateView):
    template_name = 'live/discussion.html'


class EpilogueView(BroadcastContextMixin, TemplateView):
    template_name = 'live/epilogue.html'


class GameView(BroadcastContextMixin, TemplateView):
    template_name = 'live/game.html'


class NotifierView(BroadcastContextMixin, TemplateView):
    template_name = 'live/notifier.html'


class PrologueView(BroadcastContextMixin, TemplateView):
    template_name = 'live/prologue.html'


class StatusView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        broadcast = Broadcast.objects.latest()
        context = {
            'is_episodic': is_episodic(),
            'is_live': bool(fetch_stream()),
            'number': broadcast.number }
        return self.render_json_response(context)
