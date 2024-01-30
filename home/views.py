from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post, Comment
from accounts.models import RelationInstance
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddUpdatePostUserForm
from django.contrib.auth.models import User
from django.contrib import messages
class HomeView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'home/index.html', {'users': users})

class UserProfile(LoginRequiredMixin, View):
    def get(self, request, pk):
        is_following = False
        user = User.objects.get(pk=pk)
        relation = RelationInstance.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            is_following=True
        posts = Post.objects.filter(user=user.id)
        return render(request, 'home/userprofile.html', {'user': user, 'posts': posts, 'is_following': is_following})



class DetailPostView(LoginRequiredMixin,View):

    def get(self, request, pk, slug):
        post = Post.objects.get(pk=pk, slug=slug)
        commens = post.comments.all()
        return render(request, 'home/detailpost.html', {'post': post, 'comments': commens})

    def post(self, request, pk, slug):
        post = Post.objects.get(pk=pk, slug=slug)
        Comment.objects.create(user=request.user, post=post, body=request.POST['body'])
        return redirect('home:home')









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



class FolowingUserView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        relation = RelationInstance.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            messages.error(request, 'you are not con following', 'danger')
            return redirect('home:profiles' , user.id)
        else:
            RelationInstance.objects.create(from_user=request.user, to_user=user)
            messages.success(request, 'follow','success')
            return redirect('home:profiles', user.id)


class UnfollowUserView(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        relation = RelationInstance.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            relation.delete()
            messages.success(request, 'unfollow', 'success')
        else:
            messages.error(request, 'you are not follow', 'danger')
        return redirect('home:profiles', user.id)






