# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from six import python_2_unicode_compatible

import django.db

# Create your models here.

@python_2_unicode_compatible
class Technique(django.db.models.Model):
    Name = django.db.models.CharField(max_length=100)

    def __str__(self):
        return self.Name



@python_2_unicode_compatible
class Meeting(django.db.models.Model):
    Time = django.db.models.DateTimeField()
    Technique = django.db.models.ForeignKey(Technique,
                                            on_delete=django.db.models.CASCADE)
    #Coordinator =
    #CoCoordinator =
    Notes = django.db.models.CharField(max_length=65536)

    def __str__(self):
        return str(self.Time)

