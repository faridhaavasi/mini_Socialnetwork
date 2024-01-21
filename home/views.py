from django.shortcuts import render
from django.views import View
from .models import Post
class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html', {})

class DetailPostView(View):

    def get(self, request, pk, slug):
        post = Post.objects.get(pk=pk, slug=slug)
        return render(request, 'home/detailpost.html', {'post': post})