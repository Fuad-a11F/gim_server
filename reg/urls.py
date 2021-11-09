from django.contrib import admin
from django.urls import path
from django.urls.conf import include



urlpatterns = [
    path('registration/', include('djoser.urls')),
    path('login/', include('djoser.urls.authtoken')),
    path('login/', include('djoser.urls.jwt')),
]
