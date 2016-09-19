#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import users
from django.contrib import auth
from django.contrib.auth.models import User
import hashlib

# Create your views here.

def login(req):
    if req.user.is_authenticated():
        return HttpResponseRedirect("/home")
    msg = ''
    if req.method=='POST':
        username = req.POST.get('username', '')
        password = req.POST.get('passwd', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
            auth.login(req, user)
        # Redirect to a success page.
            return HttpResponseRedirect("/home")
        else:
        # Show an error page
            msg = '请输入正确的账号密码' 
            return render_to_response("login.html",{'msg':msg},context_instance=RequestContext(req))
    
    return render_to_response("login.html",{'msg':msg},context_instance=RequestContext(req))

def logout(request):
    try:
        auth.logout(request)
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def validateInput(username,passwd):
    msg = ''
    if (not username) or username == u'账号/邮箱':
        return "username shouldn't be empty"
    if (not passwd) or passwd == u'密码':
        return "passwd shouldnlt be empty"
    if User.objects.filter(username=username):
        return "acount used"
    
    
def regist(req):
    
    if req.user.is_authenticated():
        return HttpResponseRedirect("/home")
    
    if req.method=='POST':
        username = req.POST.get('username', '')
        password = req.POST.get('passwd', '')
        #password = hashlib.md5(password).hexdigest()
        msg = validateInput(username, password)
        if msg:
            return render_to_response("regist.html",{'msg':msg},context_instance=RequestContext(req))
        else:
            user = User.objects.create(username = username)
            user.set_password(password)
            user.is_staff = True
            user.save()
            return HttpResponse('success!')
    else:
        HttpResponseRedirect('/user/login/')
        
    return render_to_response("regist.html",context_instance=RequestContext(req))
'''
class UserForm(forms.Form):
    username = forms.CharField(label='Username',max_length=12)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())
    
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = hashlib.md5(uf.cleaned_data['password']).hexdigest()
            
            users.objects.create(username = username,password=password)
            
            return HttpResponse('success!')
        
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

def login(req):
    if req.method =='POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = hashlib.md5(uf.cleaned_data['password']).hexdigest()
            
            user = users.objects.filter(username__exact = username,password__exact = password)
            
            if user:
                response = HttpResponseRedirect('/home/')
                
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/users/login')
    else:
        uf = UserForm()
            
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))
    '''
   