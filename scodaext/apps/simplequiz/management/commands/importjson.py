import os.path
import json
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from scodaext.apps.simplequiz.models import Quiz,Question,Answer

class Command(BaseCommand):
    args="<file1> <file2> ..."
    help="Imports json formatted quizzes"

    def handle(self,*args, **options):
        for fn in args:
            with open(fn) as f:
                data = json.load(f)
            q = Quiz()
            q.name = data["title"]
            q.description =data["description"]
            q.slug = slugify(
                unicode(os.path.basename(fn).replace(".json",""))
                )
            q.save()
            for qd in data["questions"]:
                qw = Question()
                qw.question = qd["question"]
                qw.quiz = q
                qw.save()
                for ad in qd["answers"]:
                    a = Answer()
                    a.question = qw
                    a.answer = ad["answer"]
                    if "correct" in ad.keys():
                        a.correct = ad["correct"]
                    else:
                        a.correct = False
                    a.save()

