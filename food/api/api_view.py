from rest_framework.response import Response
from food.api.serializer import DraftFoodSerializer, FoodDetailSerializer, FoodSerializer, FoodTrainingDetailSerializer, FoodTrainingItemSerializer, FoodTrainingItemsSerializer, FoodTrainingSerializer
from food.models import DraftFood, Food, FoodTrainingItem, ProgramFood
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from gim.models import ProgramTrainingItem
from users.models import CustomUser

class FoodApi(ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):
        if len(self.request.GET) == 0:
            return Food.objects.all()

        if self.request.GET.get('search') != None:
            return Food.objects.filter(title__icontains=self.request.GET.get('search'))

        query_set = []

        for k, l in self.request.GET.items():
            if k == 'drink':
                food = True if self.request.GET.get('food') == 'true' else False
                drink = True if self.request.GET.get('drink') == 'true' else False
                
                if food and drink:
                    query_set = Food.objects.all()

                elif food and not drink:
                    query_set = Food.objects.filter(type='eat')

                elif drink and not food:
                    query_set = Food.objects.filter(type='drink')

            if k == 'price_min':
                if 'price_max' in self.request.GET.keys():
                    query_set = query_set.filter(price__gte=l, price__lte=self.request.GET.get('price_max'))
                else:
                    query_set = query_set.filter(price__gte=l)

            if k == 'proteins_min':
                if 'proteins_max' in self.request.GET.keys():
                    query_set = query_set.filter(proteins__gte=l, proteins__lte=self.request.GET.get('proteins_max'))
                else:
                    query_set = query_set.filter(proteins__gte=l)

            if k == 'fats_min':
                if 'fats_max' in self.request.GET.keys():
                    query_set = query_set.filter(fats__gte=l, fats__lte=self.request.GET.get('fats_max'))
                else:
                    query_set = query_set.filter(fats__gte=l)

            if k == 'carbohydrates_min':
                if 'carbohydrates_max' in self.request.GET.keys():
                    query_set = query_set.filter(carbohydrates__gte=l, carbohydrates__lte=self.request.GET.get('carbohydrates_max'))
                else:
                    query_set = query_set.filter(carbohydrates__gte=l)

        return query_set


class FoodDetailApi(ListAPIView):
    def get(self, request, id):
        queryset = Food.objects.get(id=id)
        serializer = FoodDetailSerializer(queryset)
        return Response(serializer.data)


class FoodTrainingCreateApi(APIView):
    def post(self, request):
        items = []
        for item in request.data.get('items'):
            items += [FoodTrainingItem.objects.create(**item)]

        if request.data.get('action') == 'Отправить':
            program = ProgramFood.objects.create(user = request.user,
                                            user_to = CustomUser.objects.get(pk=request.data.get('user_to')),
                                            text = request.data.get('text'))

        elif request.data.get('action') == 'Сохранить':
            program = DraftFood.objects.create(user = request.user,
                                            text = request.data.get('text'))

        elif request.data.get('action') == 'Отправить и сохранить':
            program1 = ProgramFood.objects.create(date = request.data.get('date'), 
                                            user = request.user,
                                            user_to = CustomUser.objects.get(pk=request.data.get('user_to')),
                                            text = request.data.get('text'))

            program2 = DraftFood.objects.create(user = request.user,
                                            text = request.data.get('text'))
            
            for item in items:
                program1.foodItems.add(item)
                program2.foodItems.add(item)
            
            return Response({'success': 'Запись успешно сохранена и отправлена'})


        for item in items:
            program.foodItems.add(item)

        return Response({'success': 'Запись успешно отправлена'})
            

class FoodTrainingApi(ListAPIView):
    serializer_class = FoodTrainingSerializer

    def get_queryset(self):
        return ProgramFood.objects.filter(user_to=self.request.user.id).order_by('-id')


class FoodTrainingDetailApi(ListAPIView):
    serializer_class = FoodTrainingDetailSerializer

    def get_queryset(self):
        return ProgramFood.objects.filter(id=self.kwargs['id'])


class FoodTrainingItemApi(ListAPIView):
    serializer_class = FoodTrainingItemsSerializer

    def get_queryset(self):
        return ProgramFood.objects.filter(pk=self.kwargs['id'])


class FoodGetActiveTrainingApi(ListAPIView):
    serializer_class = FoodTrainingItemSerializer

    def get_queryset(self):
        return ProgramFood.objects.filter(isActive=True, user_to=self.request.user.id)


class FoodDeleteActiveTrainingApi(APIView):
    def put(self, request, id):
        active = ProgramFood.objects.get(id=id)
        active.isActive = False
        active.save()
        return Response(FoodTrainingSerializer(active).data)


class FoodSetActiveTrainingApi(APIView):
    def put(self, request):
        active_not = ProgramFood.objects.filter(user_to=request.user, isActive=True)
        if len(active_not) != 0:
            active_not[0].isActive = False
            active_not[0].save()
        active = ProgramFood.objects.get(id=request.data['id'])
        active.isActive = True
        active.save()
        return Response(FoodTrainingSerializer(active).data)


class DraftFoodApi(ListAPIView):
    serializer_class = DraftFoodSerializer

    def get_queryset(self):
        return DraftFood.objects.filter(user=self.request.user.id)


class GetFoodActive(ListAPIView):
    serializer_class = DraftFoodSerializer

    def get_queryset(self):
        return DraftFood.objects.filter(user=self.request.user.id)