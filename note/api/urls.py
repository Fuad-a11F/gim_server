from django.urls import path
from .api_view import *


urlpatterns = [
    path('get_note/', NoteApi.as_view()),
    path('create_note/', CreateNoteApi.as_view()),
    path('update_note/', UpdateNoteApi.as_view()),
    path('delete_note/<int:pk>', DeleteNoteApi.as_view()),
    path('count_note/', CountNoteApi.as_view())
]
