from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.context import RequestContext
from scodaext.apps.feedbackform.models import Feedback, Event
from scodaext.apps.feedbackform.forms import FeedbackForm

# Create your views here.

@xframe_options_exempt
def fbform(request):
    if request.method == "POST":
        f = FeedbackForm(request.POST,instance=Feedback())
        if f.is_valid():
            i = f.save()
            c = {}
            if i.event:
                e = i.event
                if i.email and e.badge_service:    
                    r = e.badge_service.issue(
                        e.badge,
                        i.email,
                        )
                    c = {"assertion": r['assertion'],
                         "badge": r['badge'] }
            return render_to_response("feedbackform/submitted.html",c,
                                      context_instance=RequestContext(request))
        else:
            c = {"form": f}
    else:
        c = {"form": FeedbackForm(),
             }
    c.update(csrf(request))
    c['form'].fields['event'].queryset = Event.objects.filter(active=True)
    return render_to_response("feedbackform/form.html",c,
                              context_instance=RequestContext(request))
