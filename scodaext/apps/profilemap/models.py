from django.db import models
from pygeocoder import Geocoder
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    foto = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name

    def geocode(self):  
        if not self.latitude:
            r = Geocoder.geocode(self.location)
            (self.latitude,self.longitude) = r[0].coordinates



@receiver(pre_save, sender=Person)
def geocode(sender, instance=None, **kwargs):
    instance.geocode()
