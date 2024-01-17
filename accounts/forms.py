from django import forms

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
        attrs={'class': 'form-control',
               'placeholder': 'enter your password'})
    )



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
        'placeholder': 'enter  username'})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'enter your password'})
    )


