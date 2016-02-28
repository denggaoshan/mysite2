#coding:utf_8
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import title

from django.contrib.auth.models import User  
from django.db.models.signals import post_save 


class Profile(models.Model):
    user = models.OneToOneField(User,unique=True)  #User 外键且唯一
    nickname = models.CharField(max_length=16,null=True, default='游客')#昵称
    
    def __unicode__(self):
        return self.nickname

    class Meta:
        db_table = 'account_profile'


def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = Profile.objects.get_or_create(user=instance)  
  
post_save.connect(create_user_profile, sender=User)  

"""
class User(models.Model):

    nickname = models.CharField(max_length=50,default="游客")
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
   
    def __str__(self):
        return self.nickname
    
    def check_password(self,pws):
        if pws == self.password:
            return True
        else:
            return False
"""

class HomePageNew(models.Model):
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=100,default="新闻")
    datetime = models.DateTimeField()
    content = models.TextField()

   
class Vote(models.Model):
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=100,default="新闻")
    datetime = models.DateTimeField()
    content = models.TextField()
    
    questions = models.ManyToManyField('Question',related_name='+',blank=True,null=True)


class Question(models.Model):
    def __str__(self):
        return self.content
    
    content = models.CharField(max_length = 100)
    
    votes =  models.ManyToManyField(Vote,
                             through=Vote.questions.through,
                             related_name='+')
    
    choices = models.ManyToManyField('Choice',related_name='+',blank=True,null=True)
    
    QUESTION_TYPE = (('S','Single'),('M','Multiple'))
    type = models.CharField(max_length=2,
                            choices=QUESTION_TYPE,
                            default='S')
 
 
class Choice(models.Model):
    def __str__(self):
        return self.content
    
    questions =  models.ManyToManyField(Question,
                             through=Question.choices.through,
                             related_name='+',blank=True,null=True)
    
    datetime = models.DateTimeField()
    content = models.TextField()