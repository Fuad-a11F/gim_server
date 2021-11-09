from django.urls import path
from .api_view import *


urlpatterns = [
    path('get_user/', GetUserApi.as_view()),
    path('get_user/<int:id>', GetUserApi.as_view()),
    path('get_user_image/', GetUserImageApi.as_view()),
    path('update_user/', UpdateUserApi.as_view()),
    path('check_password/<str:password>', CheckUserPasswordApi.as_view()),
    path('get_id/', GetIdUserApi.as_view()),
    path('get_user_contacts/<int:id>', GetContactsUserApi.as_view()),
    path('check_user/<int:id>', CheckUserApi.as_view()),
    path('check_user_friend/<int:id>', CheckUseFriendApi.as_view()),
    path('check_position/', CheckPositionApi.as_view()),
]
