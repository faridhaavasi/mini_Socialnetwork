from django import forms
from  django.contrib.auth.models import User
from django.core.validators import ValidationError
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
        'placeholder': 'enter  username'})
    )
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
        'placeholder': 'enter your email'})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'enter your password'}))
    password2 = forms.CharField(label='respect pssword' ,widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'enter your password'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password and password2:
            if password != password:
                self.add_error('password2','passoerd is not match')

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('username is invalid')
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        email_user =  User.objects.filter(email=email).exists()
        if email_user:
            raise ValidationError('email is invalid')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
        'placeholder': 'enter  username'})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'enter your password'})
    )


