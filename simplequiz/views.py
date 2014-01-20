from django.shortcuts import render_to_response, \
    get_object_or_404
from django.core.context_processors import csrf
from simplequiz.models import Quiz

def start(request):
    data = {}
    return render_to_response("start.html", data)


def quiz(request,slug):
   q = get_object_or_404(Quiz,slug=slug)
   c = {"quiz": q}
   c.update(csrf(request))
   return render_to_response("quiz.html", c)
