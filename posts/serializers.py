from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from posts.models import Post


class CreatePostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150, required=True)
    body = serializers.CharField(max_length=2000, required=True)

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post

    def validate(self, attrs):
        title = attrs['title']
        body = attrs['body']
        if title and body:
            return attrs
