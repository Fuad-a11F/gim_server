from rest_framework import serializers
from music.models import FavoriteMusic, Music, Playlist
from users.models import CustomUser

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'music', 'title']
        URL_FIELD_NAME = 'music'
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'lastname', 'position']


class PlaylistSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    music_count = serializers.IntegerField()

    class Meta:
        model = Playlist
        fields = ('id', 'user', 'title', 'music_count')


class PlaylistSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class PlaylistItemSerializer(serializers.ModelSerializer):
    music = MusicSerializer(many=True)
    class Meta:
        model = Playlist
        fields = ('music',)


class PlaylistSerializerAddMusic(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class FavoriteMusicSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = FavoriteMusic
        fields = '__all__'


class FavoriteMusicSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMusic
        fields = '__all__'