from django.db import models
from scodaext.apps.badgeclient.models import BadgeService


class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey('Question')
    correct = models.BooleanField()

    def __unicode__(self):
        return self.answer


class Question(models.Model):
    question = models.TextField()
    quiz = models.ForeignKey('Quiz')

    @property
    def answers(self):
        return Answer.objects.filter(question=self)

    def __unicode__(self):
        return self.question


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    badge = models.SlugField(null=True,blank=True)
    badge_service = models.ForeignKey(BadgeService,null=True,blank=True)
    min_right = models.IntegerField(default=70,blank=True)

    @property
    def questions(self):
        return Question.objects.filter(quiz=self)

    def __unicode__(self):
        return self.name


class Submission(models.Model):
    quiz = models.ForeignKey('Quiz')
    email = models.CharField(max_length=200)
    submission = models.TextField()
    correct = models.DecimalField(max_digits=5, decimal_places=2)
    submitted = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s-%s" % (self.quiz, self.submitted.isoformat())
