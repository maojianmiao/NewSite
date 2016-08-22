from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import users
import hashlib

# Create your views here.

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
    
def logout(req):
    response = HttpResponse('logout!!')
    response.delete_cookie('username')
    return response
            