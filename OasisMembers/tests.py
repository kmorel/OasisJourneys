# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.test
import django.urls
import django.utils

# Models testing classes

import models

class MemberModelTests(django.test.TestCase):
    def test_full_name_methods(self):
        """Test that NameFirstLast, NameLastFirst, and FullName methods
return names as expected.
"""
        newMember = models.Member(FirstName='John', LastName='Doe')
        self.assertEqual(newMember.NameFirstLast(), 'John Doe')
        self.assertEqual(newMember.NameLastFirst(), 'Doe, John')
        self.assertEqual(newMember.FullName(), 'John Doe')

# Views testing classes

import views

class MembersViewTests(django.test.TestCase):
    fixtures = [ 'testdata.json' ]

    def test_list_of_members(self):
        """Test the view with a list of members."""
        response = self.client.get(django.urls.reverse('OasisMembers:members'))
        self.assertContains(response, 'Colin Fry')
        self.assertContains(response, '<title>Oasis Journeys Members</title>')

class MemberViewTests(django.test.TestCase):
    fixtures = [ 'testdata.json' ]

    def test_member_detail(self):
        """Test the view with the detail for a single member."""
        response = self.client.get(django.urls.reverse(
            'OasisMembers:member',
            kwargs={'member_id':1}))
        self.assertContains(response, '<h1>Sylvia Browne</h1>', html=True)
        self.assertContains(response,
                            '<title>Oasis Member Sylvia Browne</title>',
                            html=True)

class MeetingsViewTests(django.test.TestCase):
    fixtures = [ 'testdata.json' ]

    def test_list_of_meetings(self):
        """Test the view with a list of meetings."""
        response = self.client.get(django.urls.reverse('OasisMembers:meetings'))
        self.assertContains(
            response,
            '<a href="/meeting/1">2017-07-01 04:58:33+00:00 - Awakening</a>',
            html=True)
        self.assertContains(
            response,
            '<title>Oasis Journeys Meetings</title>',
            html=True)

class MeetingViewTests(django.test.TestCase):
    fixtures = [ 'testdata.json' ]

    def test_meeting_detail(self):
        """Test the view with the detail for a single meeting."""
        response = self.client.get(django.urls.reverse(
            'OasisMembers:meeting',
            kwargs={'meeting_id':6}))
        self.assertContains(response, 'Meeting @ July 5, 2017')
        self.assertContains(response, '<title>Oasis Meeting @')

