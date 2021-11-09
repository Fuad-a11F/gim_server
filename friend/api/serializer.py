from friend.models import Friend
from ..models import *
from rest_framework import serializers
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'lastname', 'image', 'position']


class FriendSerializer(serializers.ModelSerializer):
    friends = UserSerializer()

    class Meta:
        model = Friend
        fields = '__all__'


