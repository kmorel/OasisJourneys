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

    def test_member_detail(self):
        """Test the view with the detail for a single member."""
        response = self.client.get(django.urls.reverse(
            'OasisMembers:member',
            kwargs={'member_id':1}))
        self.assertContains(response, '<h1>Sylvia Browne</h1>', html=True)

