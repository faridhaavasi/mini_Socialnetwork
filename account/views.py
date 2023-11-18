from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserRegisterForm
# Create your views here.

class UserRegisterView(View):
    form_class = UserRegisterForm
    temlpate_name = 'account/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.temlpate_name, {'form': form})
    def post(self, request):
        form = self.form_class(data=request.POST)
        

        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            login(request, user)
            return redirect('/')
        return render(request, self.temlpate_name, {'form': form})