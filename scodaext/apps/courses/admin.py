from django.contrib import admin
from scodaext.apps.courses.models import *

# Register your models here.

admin.site.register(Module)
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Skill)
admin.site.register(Tool)
admin.site.register(Tag)
admin.site.register(Audience)
admin.site.register(CourseModule)
