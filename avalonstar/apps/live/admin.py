# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['text', 'subtext']
admin.site.register(Message, MessageAdmin)
