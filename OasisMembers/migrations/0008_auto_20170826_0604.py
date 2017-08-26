# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 12:04
from __future__ import unicode_literals

from django.db import migrations


def MoveCoordinatorFields(apps, schema_editor):
    # We cannot import models directly as it may be a newer version than
    # this migration expects. We use the historic version.
    Meeting = apps.get_model('OasisMembers', 'Meeting')
    Attendee = apps.get_model('OasisMembers', 'Attendee')
    for meeting in Meeting.objects.all():
        if meeting.Coordinator != None:
            attendee, created = Attendee.objects.get_or_create(
                Meeting=meeting,
                Member=meeting.Coordinator)
            attendee.IsCoordinator = True
            attendee.save()
            meeting.Coordinator = None
        if meeting.CoCoordinator != None:
            attendee, created = Attendee.objects.get_or_create(
                Meeting=meeting,
                Member=meeting.CoCoordinator)
            attendee.IsCoordinator = True
            attendee.save()
            meeting.CoCoordinator = None
        meeting.save()


class Migration(migrations.Migration):

    dependencies = [
        ('OasisMembers', '0007_auto_20170825_1949'),
    ]

    operations = [
        migrations.RunPython(MoveCoordinatorFields)
    ]