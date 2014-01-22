from django.db import models
from badgeclient.models import BadgeService

# Create your models here.


class Feedback(models.Model):
    event = models.CharField(
        "Which event did you attend?",
        max_length=200,
        null=True,
        blank=True,
        )
    name = models.CharField(
        "Your Name",
        max_length=200,
        null=True,
        blank=True,
        )
    email = models.EmailField(
        "Your email address",
        null=True,
        blank=True,
        )
    nationality = models.CharField(
        "Nationality",
        max_length=200,
        null=True,
        blank=True,
        )
    worthwile = models.CharField(
        "It was worthwile for me attending the event",
        max_length=50,
        choices=[(1,"Strongly disagree"),
                 (2,"Disagree"),
                 (3,"Neither"),
                 (4,"Agree"),
                 (5,"Strongly Agree"),
                 ]
        )
    useful = models.CharField(
        "I learned something useful",
        max_length=50,
        choices=[(1,"Strongly disagree"),
                 (2,"Disagree"),
                 (3,"Neither"),
                 (4,"Agree"),
                 (5,"Strongly Agree"),
                 ]
        )
    empowered = models.CharField(
        "I feel more empowered to use data effectively",
        max_length=50,
        choices=[(1,"Strongly disagree"),
                 (2,"Disagree"),
                 (3,"Neither"),
                 (4,"Agree"),
                 (5,"Strongly Agree"),
                 ]
        )
    organise = models.CharField(
        "I am likely to organise a similar event in my community",
        max_length=50,
        choices=[(1,"Strongly disagree"),
                 (2,"Disagree"),
                 (3,"Neither"),
                 (4,"Agree"),
                 (5,"Strongly Agree"),
                 ]
        )
    learned = models.TextField(
        "What is the main thing you have learned today?",
        null=True,
        blank=True,
        )
    improve = models.TextField(
        "What is the main thing we should improve for the next event?",
        null=True,
        blank=True,
        )
    testimonial = models.TextField(
        """Leave a brief testimonial to future learners so we can spread the
        word:""",
        null=True,
        blank=True,
        )
