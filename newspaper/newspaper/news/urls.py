from django.conf.urls import url
from newspaper.news.views import *

urlpatterns = [
    url(r'^$', news_list, name='news_list'),
    url(r'^news_list/', news_list, name='news_list')
]

