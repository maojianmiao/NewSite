#coding:utf-8
'''
Created on 2016-9-25

@author: jm
'''
from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    mail = models.EmailField()
    number = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.username