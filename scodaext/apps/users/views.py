import hashlib
from django.shortcuts import render_to_response, \
    get_object_or_404
from django.core.context_processors import csrf
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.context import RequestContext 
from django.http import HttpResponseRedirect
from django.utils.html import conditional_escape
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.utils.translation import ugettext_lazy as _
from scodaext.apps.users.models import *
from scodaext.apps.users.forms import EditProfileForm, CaptchaUserCreationForm
from scodaext.apps.users.util import add_activity
# Create your views here.

def start(request):
    return render_to_response("users/start.html",{},
                               context_instance=RequestContext(request))


def new(request):
    if request.method == 'POST':    
        form = CaptchaUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/user/%s/"%new_user.username)
    else:
            form = CaptchaUserCreationForm()
        
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
    profileuser = get_object_or_404(User, username= username)
    if profileuser.email:
        gurl = "https://www.gravatar.com/avatar/%s"%hashlib.md5(profileuser.email).hexdigest()
    else:   
        gurl = "http://www.gravatar.com/avatar/goo"
    try:
        profile = Profile.objects.get(user = profileuser);
    except Profile.DoesNotExist:
        profile = None
    activities = Activity.objects.filter(user = profileuser).order_by('-date')[:20]
    c={"profileuser" : 
        profileuser,
        "gurl": gurl,
        "profile":
         profile ,
         "activities": activities}
    return render_to_response("users/profile.html",c,
                               context_instance=RequestContext(request))
@login_required
def editprofile(request):
    try:
        profile = Profile.objects.get(user = request.user) 
    except Profile.DoesNotExist:
        profile = Profile(user = request.user)
    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid(): 
            # do the changes!
            u= request.user
            u.last_name = form.cleaned_data['last_name']
            u.first_name = form.cleaned_data['first_name']
            u.email = form.cleaned_data['email']
            u.save()
            profile.description = conditional_escape(form.cleaned_data['description'])
            profile.save()
            return HttpResponseRedirect("../%s/"%u.username)
    else:
        try:
            profile = Profile.objects.get(user = request.user) 
        except Profile.DoesNotExist:
            profile = Profile()
        form = EditProfileForm(
            {"last_name": request.user.last_name,
             "first_name": request.user.first_name,
             "email": request.user.email,
             "description": profile.description,})
    c={"form": form}
    c.update(csrf(request))
    return render_to_response("users/editprofile.html", c, 
        context_instance=RequestContext(request))

@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user= request.user, data = request.POST)
        if form.is_valid():
            # do stuff
            form.save()
            return HttpResponseRedirect("../%s/"%request.user.username)
    else:
        form = PasswordChangeForm(user = request.user)
    c={"form": form}
    c.update(csrf(request))
    return render_to_response("users/password.html", c,
        context_instance=RequestContext(request))

def badges(request,username):
    profileuser = User.objects.get(username = username);
    gurl = "https://www.gravatar.com/avatar/%s"%hashlib.md5(profileuser.email).hexdigest()
    try:
        profile = Profile.objects.get(user = profileuser);
    except Profile.DoesNotExist:
        profile = None
    badges = []
    c={"profileuser" : 
        profileuser,
        "gurl": gurl,
        "profile":
         profile ,
         "badges": badges}
    return render_to_response("users/badges.html",c,
                               context_instance=RequestContext(request))
