from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Likes, Post
from posts.serializers import CreatePostSerializer


class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreatePostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Post was created!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AddLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        user = request.user
        if Likes.objects.filter(user=request.user, post=post).exists():
            return Response({'message': 'You already liked this post'}, status=status.HTTP_200_OK)
        else:
            Likes.objects.create(user=user, post=post)
            return Response({'message': 'You have liked this post'}, status=status.HTTP_200_OK)


class RemoveLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        try:
            Likes.objects.get(user=request.user, post=post).delete()
            return Response({'message': 'Removed like from this post'}, status=status.HTTP_200_OK)
        except Likes.DoesNotExist:
            return Response({'message': "You didn't like this post"}, status=status.HTTP_200_OK)
