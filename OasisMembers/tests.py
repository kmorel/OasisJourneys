# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import django.contrib.auth.models
import django.test
import django.urls
import django.utils

# Models testing classes

import models

class OasisMembersBaseTest(django.test.TestCase):
    fixtures = [ 'testdata.json' ]

    def setUp(self):
        self.factory = django.test.RequestFactory()
        self.user = \
            django.contrib.auth.models.User.objects.create_user(
                username='jdoe', email='jdoe@nowhere.com', password='secret')

    def get_request(self, url):
        request = self.factory.get(url)
        request.user = self.user
        return request


class MemberModelTests(OasisMembersBaseTest):
    def test_full_name_methods(self):
        """Test that NameFirstLast, NameLastFirst, and FullName methods
return names as expected.
"""
        newMember = models.Member(FirstName='John', LastName='Doe')
        self.assertEqual(newMember.NameFirstLast(), 'John Doe')
        self.assertEqual(newMember.NameLastFirst(), 'Doe, John')
        self.assertEqual(newMember.FullName(), 'John Doe')

    def test_attendance_per_technique(self):
        """Test that the AttendancePerTechnique method behaves as expected."""
        member = models.Member.objects.get(pk=1) # Sylvia Browne
        techniqueAttendance = member.AttendancePerTechnique()
        taList = list(techniqueAttendance)
        self.assertEqual(len(taList), models.Technique.objects.all().count())
        # First value has no meetings
        self.assertEqual(taList[0].NumMeetings, 0)
        # Last value is Testing Waters and has 2 meetings
        self.assertEqual(taList[-1].Name, 'Testing Waters')
        self.assertEqual(taList[-1].NumMeetings, 2)
        # Second to last value has one meeting
        self.assertEqual(taList[-2].NumMeetings, 1)

class TechniqueModelTests(OasisMembersBaseTest):
    def test_member_attendance(self):
        """Test that the MemberAttendance method behaves as expected."""
        technique = models.Technique.objects.get(Name='Testing Waters')
        memberAttendance = technique.MemberAttendance()
        maList = list(memberAttendance)
        self.assertEqual(len(maList), models.Member.Current().count())
        # First value has no meetings
        self.assertEqual(maList[0].NumMeetings, 0)
        # Last value is Sylvia Browne and has 2 meetings
        self.assertEqual(maList[-1].FullName(), 'Sylvia Browne')
        self.assertEqual(maList[-1].NumMeetings, 2)
        # Second to last value has one meeting
        self.assertEqual(maList[-2].NumMeetings, 1)

# Views testing classes

import views

class MembersViewTests(OasisMembersBaseTest):
    def test_list_of_members(self):
        """Test the view with a list of members."""
        request = self.get_request(django.urls.reverse('OasisMembers:members'))
        response = views.members(request)
        self.assertContains(response, 'Colin Fry')
        self.assertContains(response, '<title>Oasis Journeys Members</title>')

class MemberViewTests(OasisMembersBaseTest):
    def test_member_detail(self):
        """Test the view with the detail for a single member."""
        request = self.get_request(django.urls.reverse('OasisMembers:member',
                                                       kwargs={'member_id':1}))
        response = views.member(request, member_id=1)
        self.assertContains(response, '<h1>Sylvia Browne</h1>', html=True)
        self.assertContains(response,
                            '<title>Oasis Member Sylvia Browne</title>',
                            html=True)
        # Check Coordinated meeting
        self.assertContains(response, ' - Awakening')
        # Check Co-Coordinated meeting
        self.assertContains(response, ' - Open House')

class MeetingsViewTests(OasisMembersBaseTest):
    def test_list_of_meetings(self):
        """Test the view with a list of meetings."""
        request = self.get_request(django.urls.reverse('OasisMembers:meetings'))
        response = views.meetings(request)
        self.assertContains(
            response,
            '<a href="/meeting/1/">2017-06-30')
        self.assertContains(
            response,
            '<title>Oasis Journeys Meetings</title>',
            html=True)

class MeetingViewTests(OasisMembersBaseTest):
    def test_meeting_detail(self):
        """Test the view with the detail for a single meeting."""
        request = self.get_request(django.urls.reverse('OasisMembers:meeting',
                                                       kwargs={'meeting_id':6}))
        response = views.meeting(request, meeting_id=6)
        self.assertContains(response, 'Meeting @ July 5, 2017')
        self.assertContains(response, '<title>Oasis Meeting @')
        # Coordinator should be there
        self.assertContains(response, 'Thomas Williams')
        # Co-Coordinator should be there
        self.assertContains(response, 'Daniel Home')
        # Attendees should be there
        self.assertContains(response, 'James Hydrick')
        self.assertContains(response, 'Colin Fry')
        self.assertContains(response, 'John Edward')
        self.assertContains(response, 'Uri Geller')

    def test_no_coordinators(self):
        """Test a view that has no coordinator or cocoordinator."""
        request = self.get_request(django.urls.reverse('OasisMembers:meeting',
                                                       kwargs={'meeting_id':2}))
        response = views.meeting(request, meeting_id=2)

class TechniquesViewTests(OasisMembersBaseTest):
    def test_list_of_techniques(self):
        """Test the view with a list of techniques."""
        request = self.get_request(
            django.urls.reverse('OasisMembers:techniques'))
        response = views.techniques(request)
        self.assertContains(
            response,
            '<a href="/technique/1/">Awakening</a>',
            html=True)
        self.assertContains(
            response,
            '<title>Oasis Journeys Techniques</title>',
            html=True)

class TechniqueViewTests(OasisMembersBaseTest):
    def test_technique_detail(self):
        """Test the view with the detail for a single technique."""
        request = self.get_request(django.urls.reverse(
            'OasisMembers:technique',
            kwargs={'technique_id':5}))
        response = views.technique(request, technique_id=5)
        self.assertContains(response, 'Testing Waters')
        self.assertContains(response, '<title>Technique Testing Waters')
        self.assertContains(response, 'Sylvia Browne')
