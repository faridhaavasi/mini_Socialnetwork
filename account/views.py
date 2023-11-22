from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
# Create your views here.

class UserRegisterView(View):
    form_class = UserRegisterForm
    temlpate_name = 'account/register.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, message='you are logined')
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        form = self.form_class
        return render(request, self.temlpate_name, {'form': form})
    def post(self, request):
        form = self.form_class(data=request.POST)
        

        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            login(request, user)
            messages.success(request, 'login')
            return redirect('/')
        return render(request, self.temlpate_name, {'form': form})

class LoginUserView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request):
        form = UserLoginForm
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            login(request, user)
            messages.success(request, 'login succesfuly')
            return redirect('/')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'loguot succsful')
        return redirect('/')    
            
        
            
        
    
            