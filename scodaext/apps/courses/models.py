from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    name= models.CharField(max_length=1024)
    description= models.TextField()

    def __unicode__(self):
        return self.name

class Topic(models.Model):
    name= models.CharField(max_length=1024)
    description= models.TextField()

    def __unicode__(self):
        return self.name

class Tool(models.Model):
    name= models.CharField(max_length=1024)
    description= models.TextField()

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name= models.CharField(max_length=1024)
    description= models.TextField()

    def __unicode__(self):
        return self.name

class Audience(models.Model):
    name= models.CharField(max_length=1024)
    description= models.TextField()

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name= models.CharField(max_length=1024)
    description= models.TextField()

    def __unicode__(self):
        return self.name

class Module(models.Model):
    name= models.CharField(max_length=1024)
    description= models.TextField()
    text= models.TextField()
    image_url= models.URLField(blank=True,null=True)
    level= models.CharField(max_length = 10, 
                            choices = [
                                       ("B","Beginner"),
                                       ("I","Intermediate"),
                                       ("A","Advanced"),
                                       ("D","There be Dragons"),
                                        ])
    course= models.ManyToManyField(Course,null=True,blank=True)
    topic= models.ManyToManyField(Topic, null=True,blank=True)
    tool= models.ManyToManyField(Tool, null=True,blank=True)
    tag= models.ManyToManyField(Tag, null=True,blank=True)
    audience= models.ManyToManyField(Audience, null=True,blank=True)
    skill= models.ManyToManyField(Skill, null=True,blank=True)
    completedby= models.ManyToManyField(User, null=True, blank=True)
    

    def __unicode__(self):
        return self.name
