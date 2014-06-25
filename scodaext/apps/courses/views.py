import json
from django.shortcuts import render
from django.shortcuts import render_to_response, \
    get_object_or_404
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.context import RequestContext 
from django.utils.translation import get_language_from_request
from django.contrib.auth.decorators import login_required
from scodaext.apps.courses.forms import *;
from scodaext.apps.courses.models import *;


# Create your views here.

def start(request):
    courses = Course.objects.all()
    data = {"courses": courses}
    return render_to_response("courses/start.html", data,
        context_instance=RequestContext(request))

def courseview(request,course):
    language= get_language_from_request(request)
    course = get_object_or_404(Course,slug=course)
    modules = [i.module for i in 
        CourseModule.objects.filter(course=course).order_by('order')]
    c={"course": course,
       "modules": modules }

    return render_to_response("courses/course.html", c,
        context_instance=RequestContext(request))

def moduleview(request,course=None,module=None):
    lang = get_language_from_request(request)
    if course:
        try:
            c = Course.objects.language(lang).get(slug=course) 
        except Course.DoesNotExist:
            c = None
    else:
        c = None
    try:
        m = Module.objects.language(lang).get(slug=module)
    except Module.DoesNotExist:
        return HttpResponseNotFound()
    c={"module": m,
       "instance": m,
       "course": c}
    return render_to_response("courses/module.html",c,
        context_instance=RequestContext(request))
        

@login_required
def editmodule(request,module):
    m = get_object_or_404(Module,slug=module)
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=m)
        form.language = get_language_from_request(request)
        if form.is_valid():
            m = form.save()
            try:
                m.contributor.get(id=request.user.id)
            except m.contributor.DoesNotExist:
                m.contributor.add(request.user)
            m.save()
            return HttpResponseRedirect("../")
    else:
        form = ModuleForm(instance=m)
    c={"form": form,
       "module": m}
    c.update(csrf(request))

    return render_to_response("courses/editmodule.html",c,
        context_instance=RequestContext(request))

@login_required
def editcourse(request,course):
    c = get_object_or_404(Course, slug=course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=c)
        form.language = get_language_from_request(request)
        if form.is_valid():
            c = form.save()
            return HttpResponseRedirect("../")
    else:
        form = CourseForm(instance =c)
    ct = {"form": form,
          "course": c}
    ct.update(csrf(request))
    return render_to_response("courses/editcourse.html", ct,
        context_instance = RequestContext(request))

@login_required
def editcoursemodule(request,course):
    course = get_object_or_404(Course, slug=course)
    coursemodules = CourseModule.objects.filter(course=course).order_by('order')
    if request.method =='POST':
        slugs=request.POST.get('slugs','').split(",")
        for (i, slug) in enumerate(slugs):
            cm = coursemodules.filter(module__slug=slug)
            if cm:
                cm=cm[0] # this doesn't handle well with multiple same modules
                cm.order=i
            else:
                module = Module.objects.get(slug=slug)
                cm=CourseModule(course=course,module=module, order=i)
            cm.save()
        slugs=set(slugs)
        cms = set([i.module.slug for i in coursemodules])
        diff = cms.difference(slugs)
        for cm in diff:
            for m in coursemodules.filter(module__slug=cm):
                m.delete()
        return HttpResponseRedirect("../../")             
    else:
        pass
    c = {"course": course,
         "coursemodules": json.dumps([
                {"name":i.module.name,
                 "slug":i.module.slug,
                 "description":i.module.description,
                 "image_url":i.module.image_url} for i in coursemodules])}
    c.update(csrf(request))
    return render_to_response("courses/editcoursemodule.html", c,
        context_instance = RequestContext(request))

@login_required
def createcourse(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/user/login")
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course=form.save()
            return HttpResponseRedirect("../%s/edit/modules/"%course.slug)
    else:
        form = CourseForm()
    c = {"form": form,
        }
    c.update(csrf(request))
    return render_to_response("courses/newcourse.html",c,
        context_instance=RequestContext(request))

@login_required
def createmodule(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            m = form.save()
            m.contributor.add(request.user)
            m.save() # not sure this is needed.
            return HttpResponseRedirect("../%s"%m.slug)
    else:
        form = ModuleForm() 

    c={"form": form}
    c.update(csrf(request))
    return render_to_response("courses/newmodule.html",c,
        context_instance=RequestContext(request))

def searchmodule(request):
    if 'q' in request.GET:
        lang=get_language_from_request(request)
        ms = Module.objects.language(lang).filter(name__icontains=request.GET.get('q'))[:10]
        r={"status":"success",
           "result": [{"name": i.name,
                       "description": i.description,
                       "image_url": i.image_url,
                       "slug": i.slug} for i in ms],
                
            } 
    else:
        r={"status":"error",
           "reason":"you did non pass a query"}
    
    return HttpResponse(json.dumps(r), content_type="application/json")
