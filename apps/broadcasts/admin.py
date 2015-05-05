# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Broadcast, Highlight, Host, Raid, Series


class HighlightInline(admin.StackedInline):
    extra = 1
    model = Highlight


class HostInline(admin.TabularInline):
    extra = 1
    model = Host


class RaidInline(admin.TabularInline):
    extra = 1
    model = Raid


class BroadcastAdmin(admin.ModelAdmin):
    inlines = [RaidInline, HostInline, HighlightInline]
    list_display = ['number', 'airdate', 'status', 'series', 'game_list']
    list_display_links = ['number']

    raw_id_fields = ['games', 'series']
    autocomplete_lookup_fields = {
        'fk': ['series'],
        'm2m': ['games']
    }

    def game_list(self, obj):
        return ", ".join([g.name for g in obj.games.all()])
admin.site.register(Broadcast, BroadcastAdmin)


class HighlightAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (('broadcast', 'twid'),)}),
        ('Details', {'fields': ('title', 'description', 'game', 'url')})
    )
    list_display = ['title', 'broadcast', 'game', 'twid', 'url']
    list_display_links = ['title', 'broadcast']

    raw_id_fields = ['broadcast', 'game']
    autocomplete_lookup_fields = {'fk': ['game']}
admin.site.register(Highlight, HighlightAdmin)


class HostAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'username', 'broadcast']
admin.site.register(Host, HostAdmin)


class RaidAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'broadcast', 'username', 'game']
admin.site.register(Raid, RaidAdmin)


class SeriesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Series, SeriesAdmin)
