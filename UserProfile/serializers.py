from rest_framework import serializers
from .models import User, Friend


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'age')


class FriendSerializer(serializers.ModelSerializer):
    friend = serializers.StringRelatedField(many=True)

    class Meta:
        model = Friend
        fields = ('name',)
