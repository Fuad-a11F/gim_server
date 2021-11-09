from django.urls import path
from .api_view import GetFiveUserApi

urlpatterns = [
    path('get_new_user/', GetFiveUserApi.as_view()),
]
