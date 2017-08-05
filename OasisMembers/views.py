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

def techniques(request):
    techniques = models.Technique.objects.all()
    return django.shortcuts.render(request,
                                   'OasisMembers/techniques.html',
                                   {'technique_list':techniques})

def technique(request, technique_id):
    technique = django.shortcuts.get_object_or_404(models.Technique,
                                                   pk=technique_id)
    return django.shortcuts.render(request,
                                   'OasisMembers/technique-detail.html',
                                   {'technique':technique})

# The login/logout views are those provided by django.contrib.auth.views,
# so we do not need to provide them here. However, once completed these
# views just redirect somewhere with no indication of what happened. Attach
# some receivers to the login/logout messages here so that a message is
# displayed on whatever page the user lands at.

import django.contrib.auth.signals
import django.dispatch
import django.contrib.messages

@django.dispatch.receiver(django.contrib.auth.signals.user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    django.contrib.messages.info(request, 'Logged in ' + str(request.user) + '.')

@django.dispatch.receiver(django.contrib.auth.signals.user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    django.contrib.messages.info(request, 'Logged out.')
