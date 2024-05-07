from django import forms

from .models import RecevieMessage

class ReciveMessageForm(forms.ModelForm):
    class Meta:
        model = RecevieMessage
        fields =['full_name','email','message',]