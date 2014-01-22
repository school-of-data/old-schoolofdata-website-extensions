from django import forms
from feedbackform.models import agree_choice
class FeedbackForm(forms.Form): 
    event = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    nationality = forms.CharField(max_length=200)
    worthwhile = forms.CharField(
        widget=forms.RadioSelect(choices=agree_choice))
    useful = forms.CharField(
        widget=forms.RadioSelect(choices=agree_choice))
    empowered = forms.CharField(
        widget=forms.RadioSelect(choices=agree_choice))
    organise = forms.CharField(
        widget=forms.RadioSelect(choices=agree_choice))
    learned = forms.CharField(widget=forms.Textarea)
    improve = forms.CharField(widget=forms.Textarea)
    testimonial = forms.CharField(widget=forms.Textarea)
