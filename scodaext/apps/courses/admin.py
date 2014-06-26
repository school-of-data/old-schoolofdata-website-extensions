from django.contrib import admin
from scodaext.apps.courses.models import *

# Register your models here.

admin.site.register(Module)
admin.site.register(Course)
admin.site.register(CourseModule)
