from rest_framework import serializers

from accounts.serializers import UserFullSerializer
from posts.models import Post, Likes


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

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


class AnalyticsSerializer(serializers.ModelSerializer):
    post = PostSerializer(many=False, read_only=True)
    user = UserFullSerializer(many=False, read_only=True)
    date = serializers.SerializerMethodField()

    class Meta:
        model = Likes
        fields = ['post', 'user', 'date']

    def get_date(self, obj):
        date = obj.date.strftime('%Y-%m-%d %H:%M:%S')
        return date
