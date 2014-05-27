from django.shortcuts import render
from django.shortcuts import render_to_response, \
    get_object_or_404
from django.core.context_processors import csrf
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.context import RequestContext 

from scodaext.apps.courses.models import *;


# Create your views here.

def start(request):
    data = {}
    return render_to_response("courses/start.html", data,
        context_instance=RequestContext(request))

def courseview(request,course):
    pass

def moduleview(request,course,module):
    pass

def editmodule(request,module):
    pass

def editcourse(request,course):
    pass

def createcourse(request):
    pass

def createmodule(request):
    pass
