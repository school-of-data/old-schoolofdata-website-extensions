from django import forms

class FeedbackForm(forms.Form): 
    event = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    nationality = forms.CharField(max_length=200)
    worthwhile = forms.CharField(max_length=50)
    useful = forms.CharField(max_length=50)
    empowered = forms.CharField(max_length=50)
    organise = forms.CharField(max_length=50)
    learned = forms.TextField()
    improve = models.TextField()
    testimonial = models.TextField()
