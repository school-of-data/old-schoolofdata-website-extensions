from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField(null=True,blank=True)

    def __unicode__(self):
        return self.user

class Activity(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)
    activity = models.TextField()
