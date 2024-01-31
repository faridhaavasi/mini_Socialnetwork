from django.contrib import admin
from .models import Post , Comment, ReplayComments, Like
# Register your models here.
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(ReplayComments)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('updated', )
    list_display = ['title', 'user']
