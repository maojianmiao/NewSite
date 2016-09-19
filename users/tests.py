from django.test import TestCase

# Create your tests here.
import unittest

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
import models
from django.contrib import auth
from django.contrib.auth import backends
from django.contrib.auth.models import User
import hashlib


class testuser(unittest.TestCase):
    def test_usermethod(self):
        a = User.objects.all()
        if a:
            print a
        else:
            print 'NONE'

        print models.users.objects.all()
    
    
if '__name__' == 'main':
    unittest.main()


