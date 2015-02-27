from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=42)
    text = models.TextField()
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)