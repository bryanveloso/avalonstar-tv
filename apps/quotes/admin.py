# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'timestamp', 'creator', 'broadcast', 'game']
admin.site.register(Quote, QuoteAdmin)
