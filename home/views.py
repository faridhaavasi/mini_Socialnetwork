from django.shortcuts import render
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html', {})

class DetailPostView(LoginRequiredMixin,View):

    def get(self, request, pk, slug):
        post = Post.objects.get(pk=pk, slug=slug)
        return render(request, 'home/detailpost.html', {'post': post})