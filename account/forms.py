from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form.contol'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form.control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form.contro;'}))
    #repeat_password = forms.CharField(widget=(forms.PasswordInput(attrs={'class': 'form.control'})))
     