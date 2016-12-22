from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# MVC
# model view and controller

class Post(models.Model):
    """
    Post object
    """
    title = models.CharField(max_length=50)  # a post tile is always needed
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return "/posts/%s/" %(self.id)
        return reverse("posts:detail", kwargs={'id': self.id})

