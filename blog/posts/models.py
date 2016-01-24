from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=200)

    created_on = models.DateTimeField(default=timezone.now())
