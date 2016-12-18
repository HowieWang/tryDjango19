from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated"]
    list_display_links = ["updated"]

    fields  = (('title', 'timestamp'), 'content')


# admin.site.register(Post)
admin.site.register(Post, PostModelAdmin)