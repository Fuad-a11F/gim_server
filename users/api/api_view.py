from rest_framework.views import APIView
from rest_framework.response import Response
from friend.models import Friend
from users.models import CustomUser
from .serializer import UserContactSerializer, UserPhotoSerializer, UserSerializer
from django.contrib.auth.hashers import check_password


class GetUserApi(APIView):
    def get(self, request, id = None):
        if (id == None):
            return Response(UserSerializer(request.user, context={'request': request}).data)

        serializer = UserSerializer(CustomUser.objects.get(id=id), context={'request': request})
        return Response(serializer.data)


class GetUserImageApi(APIView):
    def get(self, request):
        serializer = UserPhotoSerializer(request.user, context={'request': request})
        return Response(serializer.data)


class CheckUserPasswordApi(APIView):
    def get(self, request, password):
        return Response(check_password(password, request.user.password))


class UpdateUserApi(APIView):
    def patch(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        print(request.data['image'])
        for key, value in request.data.items():
            setattr(user, key, value)
        user.save()
        return Response('updated')


class GetIdUserApi(APIView):
    def get(self, request):
        return Response(request.user.id)


class GetContactsUserApi(APIView):
    def get(self, request, id):
        serializer = UserContactSerializer(CustomUser.objects.get(id=id))
        return Response(serializer.data)


class CheckUserApi(APIView):
    def get(self, request, id):
        print(id)
        if request.user.id == id:
            return Response(True)
        return Response(False)


class CheckUseFriendApi(APIView):
    def get(self, request, id):
        friend = Friend.objects.filter(friends=id, me=request.user.id, is_friend=True)
        if (friend):
            return Response(True)
        return Response(False)


class CheckPositionApi(APIView):
    def get(self, request):
        return Response(request.user.position)
