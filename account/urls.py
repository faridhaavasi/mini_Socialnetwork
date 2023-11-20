from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('login', views.LoginUserView.as_view(), name='login'),
    path('logout', views.UserLogoutView, name='logout'),
]
