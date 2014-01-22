from django.contrib import admin
from feedbackform.models import Feedback, Event
from feedbackform.actions import export_to_csv

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    actions = [export_to_csv, ]


admin.site.register(Event)
admin.site.register(Feedback,FeedbackAdmin)

