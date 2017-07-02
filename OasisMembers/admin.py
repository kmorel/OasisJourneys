# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib

import models

# Register your models here.

django.contrib.admin.site.register(models.Member)
django.contrib.admin.site.register(models.Technique)
django.contrib.admin.site.register(models.Meeting)
django.contrib.admin.site.register(models.Attendee)
