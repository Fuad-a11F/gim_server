from django.urls import path
from .api_view import *

urlpatterns = [
    path('get_music/', MusicApi.as_view()),
    path('get_playlist/', PlaylistApi.as_view()),
    path('get_playlist_item/<int:id>', PlaylistItemApi.as_view()),
    path('create_playlist/', PlaylistApiCreate.as_view()),
    path('create_playlist_item/', PlaylistApiCreateAddMusic.as_view()),
    path('get_favorite_item/', FavoriteMusicApi.as_view()),
    path('create_favorite_item/', FavoriteMusicApiCreate.as_view()),

]
