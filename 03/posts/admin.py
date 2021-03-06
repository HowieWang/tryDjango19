from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated"]
    list_display_links = ["updated"]
    list_editable = ['title']
    list_filter = ['updated', 'timestamp']

    fields  = (('title', 'timestamp'), 'content')
    search_fields = ['title', 'content']

    class Meta:
        model = Post

# admin.site.register(Post)
admin.site.register(Post, PostModelAdmin)