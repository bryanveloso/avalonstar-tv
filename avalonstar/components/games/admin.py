# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Game, Platform


class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'platform', 'gbid', 'is_abandoned', 'is_completed']

    raw_id_fields = ['platform']
    autocomplete_lookup_fields = { 'fk': ['platform'] }
admin.site.register(Game, GameAdmin)


class PlatformAdmin(admin.ModelAdmin):
    pass
admin.site.register(Platform, PlatformAdmin)
