from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name = 'account'
urlpatterns = [
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('login', views.LoginUserView.as_view(), name='login'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    #API
    path('registerAPI', views.RegisterApiview.as_view(), name='registerApi'),
    path('loginAPI', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/API', TokenRefreshView.as_view(), name='token_refresh'),

]
