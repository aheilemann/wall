from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.CharField(max_length=42)
    text = models.TextField()
    email = models.EmailField(max_length=75, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.text


class UserBlacklist(models.Model):
    user = models.OneToOneField('auth.User')
    ban_reason = models.TextField()
    banned_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return str(self.user)
