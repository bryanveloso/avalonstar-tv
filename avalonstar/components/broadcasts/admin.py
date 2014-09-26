# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Broadcast, Series


class BroadcastAdmin(admin.ModelAdmin):
    pass
admin.site.register(Broadcast, BroadcastAdmin)


class SeriesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Series, SeriesAdmin)
