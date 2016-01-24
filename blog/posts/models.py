from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=50, default='')

    created_on = models.DateTimeField(default=timezone.now())
    published_on = models.DateTimeField(null=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')

    text = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
