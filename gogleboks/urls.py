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
    url(r'^review/new/(?P<bid>[a-zA-Z0-9-_]+)/$', views.review_new, name='review_new'),
    url(r'^review/(?P<pk>[0-9]+)/edit/$', views.review_edit, name='review_edit'),
    url(r'^review/(?P<pk>[0-9]+)/delete/$', views.review_delete, name='review_delete'),
    url(r'^search$', views.book_search, name='book_search'),
    url(r'^book/(?P<bid>[a-zA-Z0-9-_]+)/$', views.book_detail, name='book_detail'),
    url(r'^book/viewer/(?P<bid>[a-zA-Z0-9-_]+)/$', views.book_viewer, name='book_viewer'),
]
