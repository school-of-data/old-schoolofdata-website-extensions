from django.shortcuts import render_to_response
from django.template.context import RequestContext 
from django.views.decorators.clickjacking import xframe_options_exempt

import json


from scodaext.apps.profilemap.models import *
# Create your views here.

@xframe_options_exempt
def map(request):
    persons = Person.objects.all()
    persons = [{"name": p.name,
                "description": p.description,
                "location": p.location,
                "image": p.foto,
                "status": p.status,
                "geo": [p.longitude,p.latitude]} 
                    for p in persons]

    c = {"persons": json.dumps(persons) }
    return render_to_response("profilemap/map.html", c,
        context_instance=RequestContext(request))
