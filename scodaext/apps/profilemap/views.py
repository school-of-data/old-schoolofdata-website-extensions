from django.shortcuts import render_to_response
from django.template.context import RequestContext 
from django.views.decorators.clickjacking import xframe_options_exempt




from scodaext.apps.profilemap.models import *
# Create your views here.

@xframe_options_exempt
def mapview(request):
    persons = Person.objects.all()
    persons = [{"name": p.name,
                "description": p.description,
                "location": p.location,
                "image": p.image,
                "geo": [p.latitude,p.longitude]} 
                    for p in persons]
    c = {"persons": persons }
    return render_to_response("profilemap/map.html", c,
        context_instance=RequestContext(request))
