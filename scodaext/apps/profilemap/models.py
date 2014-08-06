from django.db import models
from pygeocoder import Geocoder
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.

@receiver(pre_save, sender=Person)
def geocode(sender, instance=None, **kwargs):
    instance.geocode()

Person(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    geo = models.CharField(max_field=500,null=True,blank=True)
    foto = models.CharField(max_lenght=1024)

    def __unicode__(self):
        return self.name

    def geocode(self):  
        if not self.geo:
            r = Geocoder.geocode(self.location)
            self.geo = str(r[0].coordinates)
