from django.contrib import admin
from feedbackform.models import Feedback
from feedbackform.actions import export_to_csv

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    actions = [export_to_csv, ]


admin.site.register(Feedback,FeedbackAdmin)
