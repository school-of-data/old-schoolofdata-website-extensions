
from hvad.forms import TranslatableModelForm
from scodaext.apps.courses.models import *

class ModuleForm(TranslatableModelForm):
    class Meta:
        model = Module
        fields = ['slug','name','description','text',
        'level','topic','tool','tag','audience','skill', 'quiz']

 
class CourseForm(TranslatableModelForm):
    class Meta:
        model = Course
        fields = ['slug', 'name', 'description']
