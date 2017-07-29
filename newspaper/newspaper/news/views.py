# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.http import HttpResponse
from django.shortcuts import render_to_response

def news_list(request):
#    return HttpResponse("Esta es mi primera respuesta")
    return render_to_response('news/news_list.html')
