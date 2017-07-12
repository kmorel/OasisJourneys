# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib

import models

class AttendeeInline(django.contrib.admin.StackedInline):
    model = models.Attendee

class MeetingAdmin(django.contrib.admin.ModelAdmin):
    fields = [
        'Time',
        'Technique',
        'Coordinator',
        'CoCoordinator',
        'Notes',
    ]
    inlines = [AttendeeInline]
    list_filter = ['Time', 'Technique']

django.contrib.admin.site.register(models.Member)
django.contrib.admin.site.register(models.Technique)
django.contrib.admin.site.register(models.Meeting, MeetingAdmin)
