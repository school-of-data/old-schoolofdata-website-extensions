from django.shortcuts import render
from django.shortcuts import render_to_response, \
    get_object_or_404
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.context import RequestContext 
from django.utils.translation import get_language_from_request
from scodaext.apps.courses.forms import *;
from scodaext.apps.courses.models import *;


# Create your views here.

def start(request):
    data = {}
    return render_to_response("courses/start.html", data,
        context_instance=RequestContext(request))

def courseview(request,course):
    pass

def moduleview(request,course=None,module=None):
    lang = get_language_from_request(request)
    try:
        m = Module.objects.language(lang).get(slug=module)
    except Module.DoesNotExist:
        return HttpResponseNotFound()
    c={"module": m}
    return render_to_response("courses/module.html",c,
        context_instance=RequestContext(request))
        

def editmodule(request,module):
    pass

def editcourse(request,course):
    pass

def createcourse(request):
    pass

def createmodule(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST);
        if form.is_valid():
            form.save()
    else:
        form = ModuleForm() 

    c={"form": form}
    c.update(csrf(request))
    return render_to_response("courses/newmodule.html",c,
        context_instance=RequestContext(request))
