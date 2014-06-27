from django.db import models
from django.contrib.auth.models import User
from hvad.models import TranslatableModel, TranslatedFields
from taggit.managers import TaggableManager
from scodaext.apps.simplequiz.models import Quiz

# Create your models here.

class Course(TranslatableModel):
    slug= models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    translations = TranslatedFields(
        name= models.CharField(max_length=1024),
        description= models.TextField(),
        )
    
    def __unicode__(self):
        return self.name
    
    class Meta():
        permissions = (("can_feature", "Can feature courses"),)




class Module(TranslatableModel):
    slug= models.SlugField(unique=True)
    translations = TranslatedFields (
        name= models.CharField(max_length=1024),
        description= models.TextField(max_length=2000),
        text= models.TextField()
        )
    image_url= models.URLField(blank=True,null=True)
    level= models.CharField(max_length = 10, 
                            choices = [
                                       ("B","Beginner"),
                                       ("I","Intermediate"),
                                       ("A","Advanced"),
                                       ("D","There be Dragons"),
                                        ])
    contributor = models.ManyToManyField(User, null=True, blank=True,
        db_table="models_contribution",related_name="contributed")
    completedby= models.ManyToManyField(User, null=True, blank=True,
        related_name="completed")
    quiz = models.ForeignKey(Quiz,blank=True,null=True)
    tags = TaggableManager(blank=True)

    

    def __unicode__(self):
        return self.name

class CourseModule(models.Model):
    course= models.ForeignKey(Course)
    module= models.ForeignKey(Module)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s - %s"%(self.course.name, self.module.name)
