from django.db import models

from accounts.models import User


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=2000)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Likes(models.Model):
    user = models.ForeignKey(User, related_name='post_likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

