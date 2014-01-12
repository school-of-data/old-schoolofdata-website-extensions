from django.shortcuts import render,render_to_response

# Create your views here.

def start(request):
  data={}
  return render_to_response("start.html",data)
