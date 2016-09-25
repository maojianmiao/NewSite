#coding:utf-8

from django.shortcuts import render
import queryDB
from django.contrib.auth.decorators import login_required
from django.core.context_processors import request
from django.http.response import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
import datetime
import time

def home(request):
    items = 25
    username = ''
    now =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    if request.user.is_authenticated():
        username = request.user.username
     
    try:
        curPage = int(request.GET.get('curPage','1'))
        allPage = int(request.GET.get('allPage','1'))
        pageType = str(request.GET.get('pageType',''))
    except ValueError:
        curPage =1
        allPage = 1
        pageType =''
    
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1
    
    startPos = (curPage - 1) *items
    endPos = startPos + items
    
    news = queryDB.queryTopic(startPos,endPos)
    #news = queryDB.queryTopic()
    if curPage == 1 and allPage == 1:
        
        counts = queryDB.query("select count(*) from Topic")[0][0]

        if counts>items and counts % items>0:
            allPage = counts/50 + 1
        if counts>items and counts % items ==0: 
            allPage = counts/50
    
    return render(request,'content.html',{'news':news,'username':username,'now':now,'allPage':allPage,'curPage':curPage})

def testSession(request):
    if request.user.is_authenticated():
        return HttpResponse(request.user.username)
    
def about(request):
    now =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    return render(request,'about.html',{'now':now})

def dobject(request):
    data = User.objects.filter(username="asdkk")
    return HttpResponse(data)

def finance(request):
    type = 5 #财经
    items = 25
    username = ''
    now =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    if request.user.is_authenticated():
        username = request.user.username
     
    try:
        curPage = int(request.GET.get('curPage','1'))
        allPage = int(request.GET.get('allPage','1'))
        pageType = str(request.GET.get('pageType',''))
    except ValueError:
        curPage =1
        allPage = 1
        pageType =''
    
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1
    
    startPos = (curPage - 1) *items
    endPos = startPos + items
    
    news = queryDB.queryTopic(startPos,endPos,type)
    #news = queryDB.queryTopic()
    if curPage == 1 and allPage == 1:
        
        counts = queryDB.query("select count(*) from Topic WHERE NewsTypeID={}".format(type))[0][0]

        if counts>items and counts % items>0:
            allPage = counts/50 + 1
        if counts>items and counts % items ==0: 
            allPage = counts/50
    
    return render(request,'content.html',{'news':news,'username':username,'now':now,'allPage':allPage,'curPage':curPage})

def tech(request):
    type = 1 #科技
    items = 25
    username = ''
    now =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    if request.user.is_authenticated():
        username = request.user.username
     
    try:
        curPage = int(request.GET.get('curPage','1'))
        allPage = int(request.GET.get('allPage','1'))
        pageType = str(request.GET.get('pageType',''))
    except ValueError:
        curPage =1
        allPage = 1
        pageType =''
    
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1
    
    startPos = (curPage - 1) *items
    endPos = startPos + items
    
    news = queryDB.queryTopic(startPos,endPos,type)
    #news = queryDB.queryTopic()
    if curPage == 1 and allPage == 1:
        
        counts = queryDB.query("select count(*) from Topic WHERE NewsTypeID={}".format(type))[0][0]

        if counts>items and counts % items>0:
            allPage = counts/50 + 1
        if counts>items and counts % items ==0: 
            allPage = counts/50
    
    return render(request,'content.html',{'news':news,'username':username,'now':now,'allPage':allPage,'curPage':curPage})  