# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_name', 'created', 'updated', 'is_active', 'is_paid', 'twid']
    list_editable = ['created', 'updated', 'is_active', 'is_paid']
    ordering = ['-updated']
admin.site.register(Ticket, TicketAdmin)
