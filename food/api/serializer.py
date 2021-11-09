from food.models import Food, FoodTrainingItem, ProgramFood, DraftFood
from rest_framework import serializers

from gim.api.serializer import UserNameSerializer


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'image', 'title']


class DraftFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = DraftFood
        fields = '__all__'


class FoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        exclude = ['image', 'title']


class FoodTrainingSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()

    class Meta:
        model = ProgramFood
        fields = ['id', 'user', 'date', 'text', 'isNew']


class FoodTrainingItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodTrainingItem
        fields = '__all__'


class FoodTrainingItemSerializer(serializers.ModelSerializer):
    foodItems = FoodTrainingItemsSerializer(many=True)

    class Meta:
        model = ProgramFood
        fields = ['foodItems']
        

class FoodTrainingDetailSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()
    foodItems = FoodTrainingItemsSerializer(many=True)

    class Meta:
        model = ProgramFood
        fields = '__all__'
        