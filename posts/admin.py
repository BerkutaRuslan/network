from django.contrib import admin

from posts.models import Post, Likes

admin.site.register(Post)
admin.site.register(Likes)
