from django.contrib import admin
from scodaext.apps.feedbackform.models import Feedback, Event
from scodaext.apps.feedbackform.actions import export_to_csv

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    actions = [export_to_csv, ]


admin.site.register(Event)
admin.site.register(Feedback,FeedbackAdmin)

