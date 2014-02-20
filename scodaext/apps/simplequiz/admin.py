from django.contrib import admin
from scodaext.apps.simplequiz.models import *
from scodaext.apps.simplequiz.actions import export_to_csv

# Register your models here.


class AnswerAdmin(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ('question', 'quiz')
    search_fields = ('question',)
    inlines = [AnswerAdmin, ]


class QuestionInline(admin.TabularInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    inlines = [QuestionInline, ]


class SubmissionAdmin(admin.ModelAdmin):
    model = Submission
    actions = [export_to_csv, ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission,SubmissionAdmin)
