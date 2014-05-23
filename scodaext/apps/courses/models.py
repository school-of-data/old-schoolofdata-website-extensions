from django.db import models
from django.contrib.auth.models import User
from hvad.models import TranslatableModel, TranslatedFields

# Create your models here.

class Course(TranslatableModel):
    slug= models.SlugField(unique=True)
    translations = TranslatedFields(
        name= models.CharField(max_length=1024),
        description= models.TextField(),
        )

    def __unicode__(self):
        return self.name

class Topic(TranslatableModel):
    translations = TranslatedFields(
        name= models.CharField(max_length=1024),
        description= models.TextField()
        )

    def __unicode__(self):
        return self.name

class Tool(TranslatableModel):
    slug= models.SlugField(unique=True)
    translations = TranslatedFields(
        name= models.CharField(max_length=1024),
        description= models.TextField()
        )

    def __unicode__(self):
        return self.name

class Tag(TranslatableModel):
    slug= models.SlugField(unique=True)
    translations = TranslatedFields(
        name= models.CharField(max_length=1024),
        description= models.TextField()
        )

    def __unicode__(self):
        return self.name

class Audience(TranslatableModel):
    slug= models.SlugField(unique=True)
    translations = TranslatedFields(
        name= models.CharField(max_length=1024),
        description= models.TextField()
        )

    def __unicode__(self):
        return self.name

class Skill(TranslatableModel):
    slug= models.SlugField(unique=True)
    translations = TranslatedFields(
        name= models.CharField(max_length=1024),
        description= models.TextField()
        )

    def __unicode__(self):
        return self.name

class Module(TranslatableModel):
    slug= models.SlugField(unique=True)
    translations = TranslatedFields (
        name= models.CharField(max_length=1024),
        description= models.TextField(),
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
    topic= models.ManyToManyField(Topic, null=True,blank=True)
    tool= models.ManyToManyField(Tool, null=True,blank=True)
    tag= models.ManyToManyField(Tag, null=True,blank=True)
    audience= models.ManyToManyField(Audience, null=True,blank=True)
    skill= models.ManyToManyField(Skill, null=True,blank=True)
    completedby= models.ManyToManyField(User, null=True, blank=True)
    

    def __unicode__(self):
        return self.name

class CourseModule(models.Model):
    course= models.ForeignKey(Course)
    module= models.ForeignKey(Module)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s - %s"%(self.course.name, self.module.name)
