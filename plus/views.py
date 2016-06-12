#coding:utf-8

from django.shortcuts import render
import queryDB
# Create your views here.

def home(request):
    news = queryDB.queryTopic()
    return render(request,'Navigation.html',{'news':news})