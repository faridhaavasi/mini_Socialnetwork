from django import forms
from .models import Post

class AddUpdatePostUserForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
