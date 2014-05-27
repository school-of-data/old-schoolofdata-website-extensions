
from django.shortcuts import render_to_response, \
    get_object_or_404
from django.core.context_processors import csrf
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.context import RequestContext 

from django.contrib.auth.models import User
from scodaext.apps.user.models import *
# Create your views here.

def start(request):
    return render_to_response("users/start.html",{},
                               context_instance=RequestContext(request))


