# -*- coding: utf-8 -*-
from django.views.generic import View

from braces.views import JSONResponseMixin

from apps.broadcasts.models import Broadcast

from .utils import fetch_stream, is_episodic


class StatusView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        broadcast = Broadcast.objects.latest()
        context = {
            'is_episodic': is_episodic(),
            'is_live': bool(fetch_stream()),
            'number': broadcast.number }
        return self.render_json_response(context)
