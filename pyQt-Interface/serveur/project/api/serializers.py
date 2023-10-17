from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Dht11


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

class Dht11Serializer(serializers.ModelSerializer) :
    class Meta :
        model = Dht11
        fields = ('data',)