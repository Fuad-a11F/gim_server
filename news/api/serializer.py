from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from ..models import LikeNew, New, Comment
from users.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'image', 'username', 'lastname']
        URL_FIELD_NAME = 'image'  


class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    likeCount = serializers.IntegerField()
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'text', 'new', 'likeCount', 'date')


class PopularCommentSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    likeCount = serializers.IntegerField()
    isLike = serializers.BooleanField()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'text', 'new', 'likeCount', 'date', 'isLike')


class CommentAllSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    likeCount = serializers.IntegerField()
    isLike = serializers.BooleanField()
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'text', 'new', 'likeCount', 'date', 'isLike')


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class NewSerializer(serializers.ModelSerializer):
    commentCount = serializers.IntegerField()

    class Meta:
        model = New
        fields = ('id', 'text', 'title', 'date', 'commentCount', 'image')


class CommentPagination(PageNumberPagination):
    page_size = 5

