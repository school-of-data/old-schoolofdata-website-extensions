from django.db import models


class BadgeService(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    app_id = models.IntegerField()
    api_key = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    badge = models.SlugField()
    badge_service = models.ForeignKey('BadgeService')

    def __unicode__(self):
        return self.name


class Question(models.Model):
    question = models.TextField()
    quiz = models.ForeignKey('Quiz')

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey('Question')
    correct = models.BooleanField()

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
