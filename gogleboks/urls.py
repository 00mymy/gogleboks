# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:30:31 2016

@author: 00mymy
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.review_list, name='review_list'),
    url(r'^review/(?P<pk>[0-9]+)/$', views.review_detail, name='review_detail'),
]
