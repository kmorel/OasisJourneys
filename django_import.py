# Run this from the django OasisJourneys directory. Before running set an
# environment variable with
#
# export DJANGO_SETTINGS_MODULE=OasisJourneys.settings

from __future__ import print_function

import django
django.setup()

import csv

from OasisMembers import models

def boolCell(strValue):
    if strValue == '0':
        return False
    else:
        return True

techniques = {}
with open('/Users/joann/Dropbox/Oasis Journeys DataBase Tables/Techniques_2017-Jun-30_0340.csv') as fd:
    reader = csv.reader(fd)
    reader.next()   # Skip header
    for row in reader:
        dbEntry, _ = models.Technique.objects.get_or_create(Name=row[1])
        techniques[row[0]] = dbEntry

members = {}
with open('/Users/joann/Dropbox/Oasis Journeys DataBase Tables/Members_2017-Jun-30_0339.csv') as fd:
    reader = csv.reader(fd)
    reader.next()   # Skip header
    for row in reader:
        dbEntry, _ = models.Member.objects.get_or_create(FirstName=row[1],
                                                         LastName=row[2])
        dbEntry.Ability1 = row[3]
        dbEntry.Ability2 = row[4]
        dbEntry.Ability3 = row[5]
        dbEntry.Ability4 = row[6]
        dbEntry.Location = row[7]
        dbEntry.IsLeader = boolCell(row[8])
        dbEntry.CourseContribution = row[9]
        dbEntry.IsCurrent = boolCell(row[10])
        try:
            dbEntry.NumberOfGuides = int(row[11])
        except ValueError:
            dbEntry.NumberOfGuides = 1
        dbEntry.LifePurpose = row[12]
        if row[13] != '':
            dbEntry.Notes = 'Plans to sell: ' + row[13]
        dbEntry.HasSpotlight = boolCell(row[14])
        dbEntry.save()
        members[row[0]] = dbEntry
