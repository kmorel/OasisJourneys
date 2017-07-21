# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from six import python_2_unicode_compatible

import django.db

# Create your models here.


@python_2_unicode_compatible
class Member(django.db.models.Model):
    ABILITIES = ( 'Feeling', 'Hearing', 'Knowing', 'Vision' )
    ABILITIES_CHOICES = ( ( ABILITIES[0], ABILITIES[0] ),
                          ( ABILITIES[1], ABILITIES[1] ),
                          ( ABILITIES[2], ABILITIES[2] ),
                          ( ABILITIES[3], ABILITIES[3] ) )
    FirstName = django.db.models.CharField('First Name', max_length=100)
    LastName = django.db.models.CharField('Last Name', max_length=100)
    Email = django.db.models.EmailField(max_length=254, blank=True)
    Ability1 = django.db.models.CharField('Ability 1',
                                          max_length=8,
                                          choices=ABILITIES_CHOICES,
                                          blank=True)
    Ability2 = django.db.models.CharField('Ability 2',
                                          max_length=8,
                                          choices=ABILITIES_CHOICES,
                                          blank=True)
    Ability3 = django.db.models.CharField('Ability 3',
                                          max_length=8,
                                          choices=ABILITIES_CHOICES,
                                          blank=True)
    Ability4 = django.db.models.CharField('Ability 4',
                                          max_length=8,
                                          choices=ABILITIES_CHOICES,
                                          blank=True)
    Location = django.db.models.CharField(max_length=200, blank=True)
    IsLeader = django.db.models.BooleanField('Leader', default=False)
    CourseContribution = django.db.models.TextField('Course Contribution', blank=True)
    IsCurrent = django.db.models.BooleanField('Current Member', default=True)
    NumberOfGuides = django.db.models.IntegerField('Number of Guides', default=1)
    LifePurpose = django.db.models.TextField('Life Purpose', blank=True)
    HasSpotlight = django.db.models.BooleanField('Spotlight', default=False)
    Notes = django.db.models.TextField(default='', blank=True)

    def NameFirstLast(self):
        return str(self.FirstName) + ' ' + str(self.LastName)

    def NameLastFirst(self):
        return str(self.LastName) + ', ' + str(self.FirstName)

    def FullName(self):
        return self.NameFirstLast()

    def __str__(self):
        return self.FullName()

    class Meta:
        ordering = ['FirstName', 'LastName']


@python_2_unicode_compatible
class Technique(django.db.models.Model):
    Name = django.db.models.CharField(max_length=100)

    def __str__(self):
        return self.Name



@python_2_unicode_compatible
class Meeting(django.db.models.Model):
    Time = django.db.models.DateTimeField()
    Technique = django.db.models.ForeignKey(
        Technique,
        on_delete=django.db.models.CASCADE)
    Coordinator = django.db.models.ForeignKey(
        Member,
        related_name='MeetingsCoordinated',
        on_delete=django.db.models.SET_NULL,
        limit_choices_to={'IsCurrent': True},
        null=True,
        blank=True)
    CoCoordinator = django.db.models.ForeignKey(
        Member,
        related_name='MeetingsCoCoordinated',
        on_delete=django.db.models.SET_NULL,
        limit_choices_to={'IsCurrent': True},
        null=True,
        blank=True)
    Notes = django.db.models.TextField(blank=True)

    def __str__(self):
        return str(self.Time) + ' - ' + str(self.Technique)


@python_2_unicode_compatible
class Attendee(django.db.models.Model):
    Meeting = django.db.models.ForeignKey(
        Meeting,
        on_delete = django.db.models.CASCADE)
    Member = django.db.models.ForeignKey(
        Member,
        on_delete = django.db.models.CASCADE,
        limit_choices_to={'IsCurrent': True})
    Notes = django.db.models.TextField(blank=True)

    def __str__(self):
        return str(self.Member) + ' @ ' + str(self.Meeting)

