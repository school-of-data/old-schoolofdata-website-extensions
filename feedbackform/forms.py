from django import forms
from feedbackform.models import Feedback

class FeedbackForm(forms.ModelForm): 
    class Meta:
        model = Feedback
        fields = ('event', 'name', 'email', 'nationality',
                  'worthwhile', 'useful', 'empowered', 
                  'organise', 'learned', 'improve', 
                  'testimonial',
                  )
        widgets = {'learned': forms.Textarea() ,
                   'improve': forms.Textarea(),
                   'testimonial': forms.Textarea(),
                   }
