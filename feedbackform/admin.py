from django.contrib import admin
from feedbackform.models import Feedback

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    actions = [export_to_csv, ]


admin.site.register(Feedback,FeedbackAdmin)
