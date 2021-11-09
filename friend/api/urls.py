from friend.api.api_view import FriendGetApi, InvitationGetApi
from .api_view import *
from django.urls import path

urlpatterns = [
    path('get_friend/', FriendGetApi.as_view()),
    path('get_invitation/', InvitationGetApi.as_view()),
    path('create_friends/', FriendCreateApi.as_view()),
    path('create_invitation/', InvitationCreateApi.as_view()),
    path('count_friend/', FriendCountApi.as_view()),
    path('count_invitation/', InvitationCountApi.as_view()),
]
