from rest_framework.views import APIView
from users.models import CustomUser
from rest_framework.generics import ListAPIView
from .serializer import UserSerializer



class GetFiveUserApi(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(position='student').order_by('-id')[:5]

