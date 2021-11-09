from rest_framework.response import Response
from friend.api.serializer import FriendSerializer
from users.models import CustomUser
from ..models import Friend
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView


class FriendGetApi(ListAPIView):
    serializer_class = FriendSerializer
    
    def get_queryset(self):
        return Friend.objects.filter(me=self.request.user, is_friend=True)


class FriendCreateApi(APIView):
    def put(self, request):
        friend = Friend.objects.get(id=request.data['id'])
        friend.is_friend = True
        friend.save()
        return Response('ok')


class InvitationGetApi(ListAPIView):
    serializer_class = FriendSerializer
    
    def get_queryset(self):
        return Friend.objects.filter(me=self.request.user, is_friend=False)


class InvitationCreateApi(CreateAPIView):
    serializer_class = FriendSerializer
    
    def post(self, request):
        friend = Friend.objects.create(me=request.user, friends=CustomUser.objects.get(id=request.data['user_id']))
        friend.save()
        return Response('ok')


class FriendCountApi(APIView):
    def get(self, request):
        friend_count = Friend.objects.filter(me=request.user, is_friend=True).count()
        return Response(friend_count)


class InvitationCountApi(APIView):
    def get(self, request):
        friend_count = Friend.objects.filter(me=request.user, is_friend=False).count()
        return Response(friend_count)



