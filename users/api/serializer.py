from rest_framework import serializers
from users.models import CustomUser
from gim.models import UserTicket


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['image', 'username', 'position', 'lastname','email','birth','phone','fathername']
        URL_FIELD_NAME = 'image'        

class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'phone', 'facebook', 'twitter', 'instagram']


class UserPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'image']
        URL_FIELD_NAME = 'image' 
             

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTicket
        fields = '__all__'
