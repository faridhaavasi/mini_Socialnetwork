from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import Registerserializer
from rest_framework.serializers import ValidationError
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

class RegisterApiview(APIView):
    serializer_class = Registerserializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            vd = serializer.validated_data
            if vd['password'] != vd['repeat_password']:
                raise ValidationError('password and repeat_password is not match')

            user = User(username=vd['username'], email=vd['email'])
            user.set_password(vd['password'])
            user.save()
            login(request, user)
            return Response({'massage': 'Registered'})
        return Response(serializer.errors)

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
            
class LogoutApiview(APIView):
    pass

            
        
    
            