from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _


from .models import MyUser

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ["phone_number",]
    def clean_password2(self):
        cd = self.cleaned_data
        if cd ['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError("passwords dont match")
        return cd['password2']

    def save(self, commit:True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text = "you can change password usign this<a href='../password/'> form</a>")

    class Meta:
        model = MyUser
        fields = ['phone_number', 'password', 'last_login']



class UserRegisterForm(forms.Form):

    phone = forms.CharField(label=_('phone number'),max_length=11, required=True)
    password = forms.CharField(label=_('password'),widget=forms.PasswordInput)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        user = MyUser.objects.filter(phone_number=phone).exists()
        if user:
            raise ValidationError('This phone number already exists')
        return phone
    

class VerifyCodeForm(forms.Form):
    code =forms.IntegerField()