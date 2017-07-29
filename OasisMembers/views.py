# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

import django.http
import django.shortcuts
import django.urls

import models

def index(request):
    return django.shortcuts.render(request, 'OasisMembers/index.html', {})

def members(request):
    member_list = models.Member.objects.all()
    context = {
        'member_list':member_list,
    }
    return django.shortcuts.render(request, 'OasisMembers/members.html', context)

def member(request, member_id):
    member = django.shortcuts.get_object_or_404(models.Member, pk=member_id)
    return django.shortcuts.render(request,
                                   'OasisMembers/member-detail.html',
                                   {'member':member})

def member_notes_edit(request, member_id):
    member = django.shortcuts.get_object_or_404(models.Member, pk=member_id)
    return django.shortcuts.render(request,
                                   'OasisMembers/member-notes-edit.html',
                                   {'member':member})

def member_notes_submit(request, member_id):
    member = django.shortcuts.get_object_or_404(models.Member, pk=member_id)
    member.Notes = request.POST['notes']
    member.save()
    return django.http.HttpResponseRedirect(
        django.urls.reverse('OasisMembers:member',
                            args=(member_id)))

def meetings(request):
    meetings = models.Meeting.objects.all()
    return django.shortcuts.render(request,
                                   'OasisMembers/meetings.html',
                                   {'meeting_list':meetings})

def meeting(request, meeting_id):
    meeting = django.shortcuts.get_object_or_404(models.Meeting, pk=meeting_id)
    return django.shortcuts.render(request,
                                   'OasisMembers/meeting-detail.html',
                                   {'meeting':meeting})

