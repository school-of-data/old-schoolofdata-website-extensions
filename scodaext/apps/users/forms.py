from django import forms
from django.utils.translation import ugettext_lazy as _

class EditProfileForm(forms.Form):
    first_name = forms.CharField(label=_("Given Name(s)"), max_length = 30, required = False)
    last_name = forms.CharField(label=_("Family Name(s)"), max_length = 30, required = False)
    email = forms.EmailField(label=_("Email"), max_length = 75, required = True)
    description = forms.CharField(label=_("Description"),
                                  widget=forms.Textarea, 
                                  required = False)


