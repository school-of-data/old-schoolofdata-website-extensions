from django.contrib import admin
from simplequiz.models import Quiz,Question,BadgeService,Answer

# Register your models here.


class AnswerAdmin(admin.TabularInline):
  model = Answer

class QuestionAdmin(admin.ModelAdmin):
  model=Question
  inlines = [AnswerAdmin, ]

class QuestionInline(admin.TabularInline):
  model=Question

class QuizAdmin(admin.ModelAdmin):
  model = Quiz
  inlines = [QuestionInline, ]

admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(BadgeService)
