# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Broadcast, Highlight, Raid, Series


class HighlightInline(admin.StackedInline):
    extra = 1
    model = Highlight


class RaidInline(admin.TabularInline):
    extra = 1
    model = Raid


class BroadcastAdmin(admin.ModelAdmin):
    inlines = [RaidInline, HighlightInline]
    list_display = ['number', 'airdate', 'status', 'series']
    list_editable = ['airdate', 'status', 'series']
    list_display_links = ['number']

    raw_id_fields = ['games', 'series']
    autocomplete_lookup_fields = {
        'fk': ['series'],
        'm2m': ['games']
    }
admin.site.register(Broadcast, BroadcastAdmin)


class RaidAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'broadcast', 'raider', 'game']
admin.site.register(Raid, RaidAdmin)


class SeriesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Series, SeriesAdmin)
