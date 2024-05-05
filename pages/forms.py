from django import forms

from .models import RecevieMessage

class ReciveMessageForm(forms.ModelForm):
    class Meta:
        model = RecevieMessage
        fields =['first_name','last_name','email','message',]