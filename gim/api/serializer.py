from gim.models import AllTickets, Draft, ProgramTraining, ProgramTrainingItem, UserTicket
from rest_framework import serializers
from users.models import CustomUser


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'lastname')


class AllTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllTickets
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()
    coach = UserNameSerializer()
    alltickets = AllTicketsSerializer()

    class Meta:
        model = UserTicket
        fields = '__all__'


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'lastname')


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'lastname', 'experience', 'about')


class CoachDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'lastname', 'experience', 'about', 'birth', 'email')


class ProgramTrainingSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()
    user_to = UserNameSerializer()

    class Meta:
        model = ProgramTraining
        exclude  = ['programItems']


class ProgramTrainingItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramTrainingItem
        fields = '__all__'


class ProgramTrainingItemSerializer(serializers.ModelSerializer):
    programItems = ProgramTrainingItemsSerializer(many=True)

    class Meta:
        model = ProgramTraining
        fields = ['programItems']


class DraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Draft
        exclude = ['programItems']


class AllTicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllTickets
        fields = '__all__'
