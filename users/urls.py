#coding:utf-8
'''
Created on 2016-7-5

@author: jm
'''

from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
                        url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^logout/$',views.logout,name = 'logout'),
                       
                       )