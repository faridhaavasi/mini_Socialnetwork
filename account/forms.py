from typing import Any
from django.forms import ValidationError
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form.contol'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form.control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form.contro;'}))
    repeat_password = forms.CharField(widget=(forms.PasswordInput(attrs={'class': 'form.control'})))
    def clean_repeat_password(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('repeat_password'):
            raise ValidationError('password and repeat password is not match')
        return self.cleaned_data.get('repeat_password')
    
    def clean(self) -> dict[str, Any]:
        user = User.objects.filter(username=self.cleaned_data.get('username')).exists()
        if user:
            raise ValidationError('username is exist')
        return super().clean()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form.contol'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form.contro;'}))

    

     