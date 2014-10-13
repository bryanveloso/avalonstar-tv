# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Broadcast, Series


class BroadcastAdmin(admin.ModelAdmin):
    list_display = ['number', 'airdate', 'status', 'series']
    list_editable = ['airdate', 'status', 'series']
    list_display_links = ['number']

    raw_id_fields = ['games', 'series']
    autocomplete_lookup_fields = {
        'fk': ['series'],
        'm2m': ['games']
    }
admin.site.register(Broadcast, BroadcastAdmin)


class SeriesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Series, SeriesAdmin)
