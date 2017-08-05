# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from newspaper.news.models import News

# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(News, NewsAdmin)
