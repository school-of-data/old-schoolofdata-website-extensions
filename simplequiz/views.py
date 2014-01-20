import re
from django.shortcuts import render_to_response, \
    get_object_or_404
from django.core.context_processors import csrf
import okbadger
from simplequiz.models import Quiz,Answer

def start(request):
    data = {}
    return render_to_response("start.html", data)


def quiz(request,slug):
    if request.method == "GET":  
        q = get_object_or_404(Quiz,slug=slug)
        c = {"quiz": q}
        c.update(csrf(request))
        return render_to_response("quiz.html", c)
    if request.method == "POST":
        post = request.POST
        q = get_object_or_404(Quiz,slug=slug)
        questions = filter(
            lambda x: re.match("[0-9]+$",x),
            post.keys()
            )
        answers = [Answer.objects.get(id=int(post[i])) 
                   for i in questions]    
        correct = sum((i.correct for i in answers))
        percent = correct/len(answers)
        if percent >= q.min_right and post['email']:
            "Issue a Badge"
            bs = q.badge_service
            bc = okbadger.Client(bs.url, bs.app_id, bs.api_key)
            resp = bc.issue(q.badge, post['email'])
            if resp["status"] == "success":
                assertion = resp["assertion"]
                badge = resp["badge"]
            else:
                assertion = None
        else:
            assertion = None
            
        c = {"keys": answers,
             "correct": correct,
             "num_questions": len(answers),
             "assertion": assertion,
             "quiz": q,
             "badge": badge,
            } 
        return render_to_response("quiz-results.html", c) 
