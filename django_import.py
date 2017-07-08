# Run this from the django OasisJourneys directory. Before running set an
# environment variable with
#
# export DJANGO_SETTINGS_MODULE=OasisJourneys.settings

from __future__ import print_function

import re

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

meetings = {}
with open('/Users/joann/Dropbox/Oasis Journeys DataBase Tables/Meetings_2017-Jun-30_0333.csv') as fd:
    reader = csv.reader(fd)
    reader.next()   # Skip header
    for row in reader:
        date = re.sub('([0-9]+)/([0-9]+)/([0-9]+)', '20\\3-\\1-\\2', row[1])
        date = date + "-06:00"
        dbEntry, _ = models.Meeting.objects.get_or_create(
            Time=date, Technique=techniques[row[0]])
        if row[2] != '':
            dbEntry.Coordinator = members[row[2]]
        if row[3] != '':
            dbEntry.CoCoordinator = members[row[3]]
        dbEntry.Notes = row[4]
        dbEntry.save()
        meetings[row[5]] = dbEntry

with open('/Users/joann/Dropbox/Oasis Journeys DataBase Tables/Attendees_2017-Jun-30_0332.csv') as fd:
    reader = csv.reader(fd)
    reader.next()   # Skip header
    for row in reader:
        if not row[0] in meetings.keys():
            print('No meeting ', row[0], '. Skipping')
            continue
        if not row[1] in members.keys():
            print('No member ', row[1], 'for meeting', row[0], '. Skipping')
            continue
        dbEntry, _ = models.Attendee.objects.get_or_create(
            Meeting=meetings[row[0]],
            Member=members[row[1]])
        dbEntry.Notes = row[2]
        dbEntry.save()
