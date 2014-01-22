from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from feedbackform.models import Feedback, Event
from feedbackform.forms import FeedbackForm

# Create your views here.

def fbform(request):
    if request.method == "POST":
        f = FeedbackForm(request.POST)
        if f.is_valid():
            pass
        else:
            c = {"form": f}
    else:
        c = {"form": FeedbackForm(),
             }
    c.update(csrf(request))
    return render_to_response("feedbackform/form.html",c)
