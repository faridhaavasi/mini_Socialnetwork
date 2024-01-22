from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddUpdatePostUserForm
from django.contrib import messages

class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html', {})

class DetailPostView(LoginRequiredMixin,View):

    def get(self, request, pk, slug):
        post = Post.objects.get(pk=pk, slug=slug)
        return render(request, 'home/detailpost.html', {'post': post})




class AddPostUserView(LoginRequiredMixin, View):
    form_class = AddUpdatePostUserForm
    template = 'home/addpostuser.html'
    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form': form})
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'added post', 'success')
            return redirect('accounts:selfprofile')
        return render(request, self.template, {'form': form})


class UpdatePostUserView(LoginRequiredMixin, View):
    form_class = AddUpdatePostUserForm
    template = 'home/updatepostuser.html'
    def setup(self, request, *args, **kwargs):
        self.instance = Post.objects.get(pk=kwargs['pk'])
        return super().setup(request,*args, **kwargs)

    def get(self, request, pk):
        form = self.form_class(instance=self.instance)
        return render(request, self.template, {'form': form})
    def post(self, request, pk):
        form = self.form_class(data=request.POST, instance=self.instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'updated post', 'success')
            return redirect('accounts:selfprofile')
        return render(request, self.template, {'form': form})
class DeletePostUserView(LoginRequiredMixin, View):
    def get(self, request, pk, slug):
        post = Post.objects.get(pk=pk)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request, 'deleted post', 'success')
        else:
            messages.error(request, 'you are con not delete post', 'danger')
        return redirect('home:home')



