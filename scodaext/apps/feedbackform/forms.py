from django import forms
from scodaext.apps.feedbackform.models import Feedback

class FeedbackForm(forms.ModelForm): 
    class Meta:
        model = Feedback
        fields = '__all__'
        widgets = {'learned': forms.Textarea() ,
                   'improve': forms.Textarea(),
                   'testimonial': forms.Textarea(),
                   }
