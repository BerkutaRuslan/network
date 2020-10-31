from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from accounts.serializers import SignUpSerializer, UserFullSerializer, SignInSerializer


class SignUpView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.validated_data['user']
            except KeyError:
                user = serializer.save()

            return Response({"message": f'Congrats, {user.username} You are in our system now!'},
                            status=status.HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SignInView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user_serializer = UserFullSerializer(user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': user_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
