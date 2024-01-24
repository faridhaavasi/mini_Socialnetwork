from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

class RegisterView(View):
    form_class = RegisterForm
    template = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
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


class LoginView(View):
    form_class = LoginForm
    template = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'], password=cd['password'])
            login(request, user)
            messages.success(request, 'you are logined', 'success')
            return redirect('home:home')
        return render(request, self.template, {'form': form})



class LogoutView(LoginRequiredMixin,View):
    
    def get(self, request):
        logout(request)
        messages.success(request, 'you are logouted', 'success')
        return redirect('home:home')



class SelfProfileUserView(View):
    template = 'accounts/selfprofile.html'
    def get(self, request):
        user = request.user
        posts = Post.objects.filter(user=user.id)
        return render(request, self.template, {'user': user, 'posts': posts})

class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
