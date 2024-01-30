from django.contrib import admin
from .models import Post , Comment
# Register your models here.
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('updated', )
    list_display = ['title', 'user']
