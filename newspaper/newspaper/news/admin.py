# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from newspaper.news.models import News, Event

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)

