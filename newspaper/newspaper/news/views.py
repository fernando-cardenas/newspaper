
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from newspaper.news.models import News

def news_list(request):
#    return HttpResponse("Esta es mi primera respuesta")
    news =  News.objects.filter(
        publish_date__lte=datetime.now()).order_by('-publish_date')
    return render_to_response('news/news_list.html',
                              {'news': news})
