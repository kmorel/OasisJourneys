# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib

import models

class MemberAdmin(django.contrib.admin.ModelAdmin):
    list_display = [
        'FullName',
        'IsCurrent',
        'HasSpotlight',
    ]
    list_filter = [ 'IsCurrent' ]

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
    date_hierarchy = 'Time'
    inlines = [AttendeeInline]
    list_filter = ['Time', 'Technique']

django.contrib.admin.site.register(models.Member, MemberAdmin)
django.contrib.admin.site.register(models.Technique)
django.contrib.admin.site.register(models.Meeting, MeetingAdmin)

django.contrib.admin.site.site_header = 'Oasis Journeys Members Admin'
