# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import django.http
import django.shortcuts

import models

def index(request):
    return django.http.HttpResponse("Hello, world.")

def members(request):
    member_list = models.GetOrderedMemberList()
    context = {
        'member_list':member_list,
    }
    return django.shortcuts.render(request, 'OasisMembers/members.html', context)

def member(request, member_id):
    member = django.shortcuts.get_object_or_404(models.Member, pk=member_id)
    return django.shortcuts.render(request,
                                   'OasisMembers/member-detail.html',
                                   {'member':member})
