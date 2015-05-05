# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Quote


class QuoteAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('text', ('timestamp', 'subject'),)}),
        ('Metadata', {'fields': ('creator', 'broadcast', 'game')})
    )
    list_display = ['text', 'timestamp', 'subject', 'creator', 'broadcast', 'game']
    list_editable = ['timestamp', 'broadcast']

    raw_id_fields = ['broadcast', 'game']
    autocomplete_lookup_fields = {'fk': ['game']}
admin.site.register(Quote, QuoteAdmin)
