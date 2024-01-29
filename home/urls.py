from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detailpost/<int:pk>/<slug:slug>', views.DetailPostView.as_view(), name='detailpost'),
    path('addpost', views.AddPostUserView.as_view(), name='addpost'),
    path('update/<int:pk>',views.UpdatePostUserView.as_view(), name='update'),
    path('delete/<int:pk>/<slug:slug>',views.DetailPostView.as_view(), name='delete'),
    path('profiles/<int:pk>', views.UserProfile.as_view(), name='profiles'),
    path('folow/<int:pk>', views.FolowingUserView.as_view(), name='follow'),
    path('unfolow/<int:pk>', views.UnfollowUserView.as_view(), name='unfollow'),
]