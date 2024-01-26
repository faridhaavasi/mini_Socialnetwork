from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class RelationInstance(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.following} - {self.to_user}'