from food.api.api_view import *
from django.urls import path

urlpatterns = [
    path('get_food/', FoodApi.as_view()),
    path('get_detail_food/<int:id>', FoodDetailApi.as_view()),
    path('get_food_program/', FoodTrainingApi.as_view()),
    path('get_food_program_detail/<int:id>', FoodTrainingDetailApi.as_view()),
    path('get_food_active_program/', FoodGetActiveTrainingApi.as_view()),
    path('delete_food_active_program/<int:id>', FoodDeleteActiveTrainingApi.as_view()),
    path('set_food_active_program/', FoodSetActiveTrainingApi.as_view()),
    path('create_food_program/', FoodTrainingCreateApi.as_view()),
    path('get_food_program_item/<int:id>', FoodTrainingItemApi.as_view()),
    path('get_draft_food/', DraftFoodApi.as_view()),
]
