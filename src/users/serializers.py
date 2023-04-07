from rest_framework import serializers
from users.models import User


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
