import re
import json
from django.shortcuts import render_to_response, \
    get_object_or_404
from django.core.context_processors import csrf
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template.context import RequestContext 

import okbadger
from scodaext.apps.simplequiz.models import Quiz, \
    Answer, Submission

def start(request):
    data = {}
    return render_to_response("simplequiz/start.html", data,
                              context_instance=RequestContext(request))

@xframe_options_exempt
def quiz(request,slug):
    if request.method == "GET":  
        q = get_object_or_404(Quiz,slug=slug)
        c = {"quiz": q,
             }
        c.update(csrf(request))
        return render_to_response("simplequiz/quiz.html", c,
                                  context_instance=RequestContext(request))

    if request.method == "POST":
        post = request.POST
        q = get_object_or_404(Quiz,slug=slug)
        questions = q.questions
        for i in questions:
            i.correct = Answer.objects.get(question=i, correct=True)
            i.answered = Answer.objects.get(id=int(post[str(i.id)]))
        answers = [i.answered for i in questions]    
        correct = sum((i.correct for i in answers))
        percent = correct/len(answers) * 100
        if percent >= q.min_right and post['email']:
            "Issue a Badge"
            bs = q.badge_service
            resp = bs.issue(q.badge, post['email'])
            if resp["status"] == "success":
                assertion = resp["assertion"]
                badge = resp["badge"]
            else:
                assertion = None
                badge = None
        else:
            assertion = None
            badge = None
        
        s = Submission()
        s.quiz = q
        s.email = post['email']
        s.submission = json.dumps(post)
        s.correct = percent 
        s.save()
        c = {"keys": answers,
             "correct": correct,
             "num_questions": len(answers),
             "assertion": assertion,
             "quiz": q,
             "badge": badge,
             "questions": questions,
            }
        return render_to_response("simplequiz/quiz-results.html", c, 
                                  context_instance=RequestContext(request))
