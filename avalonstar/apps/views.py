# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class PlainTextView(TemplateView):
    def render_to_response(self, context, **kwargs):
        return super(TemplateView, self).render_to_response(context, content_type='text/plain', **kwargs)
