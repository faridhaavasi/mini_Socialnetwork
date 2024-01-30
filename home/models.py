from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super().save()

    def get_absolut_url(self):
        return reverse('home:detailpost', args=[self.pk, self.slug])


    def __str__(self):
        return f'{self.title} - {self.user.username}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comments for post{self.post} by {self.user}'




class ReplayComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replays')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replays')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'replay comment : {self.comment} in user {self.user}'














