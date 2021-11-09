from rest_framework.response import Response
from music.api.serializer import FavoriteMusicSerializerCreate, MusicSerializer, PlaylistSerializer, PlaylistSerializerCreate, FavoriteMusicSerializer
from music.models import FavoriteMusic, Music, Playlist
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from django.db.models import Count


class MusicApi(APIView):
    def get(self, request):
        queryset = Music.objects.all()
        return Response(MusicSerializer(queryset, many=True, context={'request': request}).data)


class PlaylistApi(ListAPIView):
    serializer_class = PlaylistSerializer
    
    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user.id).annotate(music_count=Count('music'))


class PlaylistItemApi(ListAPIView):
    serializer_class = MusicSerializer
    
    def get_queryset(self):
        return Music.objects.filter(playlist=self.kwargs['id'])


class PlaylistApiCreate(APIView):
    def post(self, request):
        playlist = Playlist.objects.create(title=request.data['title'], user=request.user)
        playlist.save()
        return Response(PlaylistSerializerCreate(playlist).data)


class PlaylistApiCreateAddMusic(APIView):
    def put(self, request):
        music = Music.objects.get(id=request.data.get('id_music'))
        prev_id = None
        if (music.playlist):
            if request.data.get('id_playlist') == music.playlist.id:
                return Response({'error': 'It was already exist there!', 'prev': None})
            prev_id = music.playlist.id
        music.playlist = Playlist.objects.get(id=request.data.get('id_playlist')) 
        music.save()
        return Response({'ok': 'success', 'prev': prev_id})


class FavoriteMusicApi(ListAPIView):
    queryset = FavoriteMusic.objects.all()
    serializer_class = FavoriteMusicSerializer


class FavoriteMusicApiCreate(CreateAPIView):
    queryset = FavoriteMusic.objects.all()
    serializer_class = FavoriteMusicSerializerCreate