from django.contrib.auth.password_validation import validate_password
from phonenumbers import is_valid_number, parse as phonenumbers_parse
from rest_framework import serializers, exceptions

from accounts.models import User


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    phone = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        phone = attrs['phone']
        password = attrs['password']
        try:
            user = User.objects.get(phone=phone)
            attrs['user'] = user
        except User.DoesNotExist:
            if is_valid_number(phonenumbers_parse(phone, None)):
                validate_password(password)
            else:
                msg = 'Must provide phonenumber in internation format'
                raise exceptions.ValidationError(msg)
        return attrs


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password == confirm_password:
            validate_password(password)
            return password
        else:
            msg = {"password": "Passwords did not match"}
            raise exceptions.ValidationError(msg)


class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone']
