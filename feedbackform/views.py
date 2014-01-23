from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from feedbackform.models import Feedback, Event
from feedbackform.forms import FeedbackForm

# Create your views here.

def fbform(request):
    if request.method == "POST":
        f = FeedbackForm(request.POST,instance=Feedback())
        if f.is_valid():
            f.save()
            try:
                e = Event.objects.get(
                    name=request.POST['event'].strip())
                if request.POST['email']:    
                    r = e.badge_service.issue(
                        e.badge,
                        request.POST['email']
                        )
                    c = {"assertion": r['assertion'],
                         "badge": r['badge'] }
                else:
                    c = {}
            except ObjectDoesNotExist:
                c = {}
            return render_to_response("feedbackform/submitted.html",c)
        else:
            c = {"form": f}
    else:
        c = {"form": FeedbackForm(),
             }
    c.update(csrf(request))
    return render_to_response("feedbackform/form.html",c)
