import hashlib
from django.shortcuts import render_to_response, \
    get_object_or_404
from django.core.context_processors import csrf
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.context import RequestContext 
from django.http import HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from scodaext.apps.users.models import *
# Create your views here.

def start(request):
    return render_to_response("users/start.html",{},
                               context_instance=RequestContext(request))


def new(request):
    if request.method == 'POST':    
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            auth.login(request,new_user)
            return HttpResponseRedirect("/user/%s/"%new_user.username)
    else:
            form = UserCreationForm()
        
    c={'form':form}
    c.update(csrf(request))
    return render_to_response("users/new.html",c,
                              context_instance=RequestContext(request))

    

def login(request):
    """ show the login form and perform the login """
    if request.user.is_authenticated():
        return HttpResponseRedirect("/user/%s/"%request.user.username)
    if request.method == 'POST':
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = auth.authenticate(username = username, 
                                 password = password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect("/user/%s/"%user.username)
        else:
            c={"username": username,
               "error": _("no such user:password combination")}
    else:
        c={}
    c.update(csrf(request))
    return render_to_response("users/login.html",c, 
                               context_instance=RequestContext(request))
        

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
    

def profile(request,username):
    print "username: %s"%username
    profileuser = User.objects.get(username = username);
    gurl = "https://www.gravatar.com/avatar/%s"%hashlib.md5(profileuser.email).hexdigest()
    try:
        profile = Profile.objects.get(user = profileuser);
    except Profile.DoesNotExist:
        profile = None
    activities = Activity.objects.filter(user = profileuser);
    c={"profileuser" : 
        profileuser,
        "gurl": gurl,
        "profile":
         profile ,
         "activities": activities}
    return render_to_response("users/profile.html",c,
                               context_instance=RequestContext(request))

def editprofile(request,username):
    pass
