from django.db import models
import okbadger

# Create your models here.

class BadgeService(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    app_id = models.IntegerField()
    api_key = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name
    
    def issue(self,badge,recipient):
        bc = okbadger.Client(self.url,self.app_id,self.api_key)
        return bc.issue(badge, recipient)
