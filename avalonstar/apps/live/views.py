# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from braces.views import JSONResponseMixin

from apps.broadcasts.models import Broadcast
from apps.live.models import Message


class BroadcastContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BroadcastContextMixin, self).get_context_data(**kwargs)
        context['broadcast'] = Broadcast.objects.latest()
        context['message_list'] = Message.objects.order_by('?')
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
        context = {'a': fetch_status()}
        return self.render_json_response(context)
