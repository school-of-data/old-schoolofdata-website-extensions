from django import forms
from feedbackform.models import Feedback

class FeedbackForm(forms.ModelForm): 
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {'learned': forms.Textarea() ,
                   'improve': forms.Textarea(),
                   'testimonial': forms.Textarea(),
                   }
