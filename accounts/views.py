from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
class RegisterView(View):
    form_class = RegisterForm
    template = 'accounts/register.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            messages.success(request, 'register successfuly', 'success')
            return redirect('home:home')
        return render(request, self.template, {'form': form})


