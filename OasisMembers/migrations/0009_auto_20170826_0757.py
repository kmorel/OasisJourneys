# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OasisMembers', '0008_auto_20170826_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='CoCoordinator',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='Coordinator',
        ),
    ]
