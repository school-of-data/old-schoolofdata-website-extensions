import re
import json
from django.shortcuts import render_to_response, \
    get_object_or_404
from django.core.context_processors import csrf
import okbadger
from scodaext.apps.simplequiz.models import Quiz, \
    Answer, Submission

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
        questions = q.questions
        for i in questions:
            i.correct = Answer.objects.get(question=i, correct=True)
            i.answered = Answer.objects.get(id=int(post[str(i.id)]))
        answers = [i.answered for i in questions]    
        correct = sum((i.correct for i in answers))
        percent = correct/len(answers)
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
        s.correct = percent * 100
        s.save()
        c = {"keys": answers,
             "correct": correct,
             "num_questions": len(answers),
             "assertion": assertion,
             "quiz": q,
             "badge": badge,
             "questions": questions,
            }
        return render_to_response("quiz-results.html", c) 
