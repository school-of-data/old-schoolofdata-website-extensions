
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
            return HttpResponseRedirect("/user/%s/"%new_user.username)
    else:
            form = UserCreationForm()
        
    c={'form':form}
    c.update(csrf(request))
    return render_to_response("users/new.html",c,
                              context_instance=RequestContext(request))

    

def login(request):
    """ show the login form and perform the login """
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
    pass

def profile(request,username):
    pass

def editprofile(request,username):
    pass
