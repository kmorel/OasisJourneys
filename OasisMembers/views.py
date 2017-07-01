# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import django.http

def index(request):
    return django.http.HttpResponse("Hello, world.")
