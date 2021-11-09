from django.urls import path
from .api_view import *

urlpatterns = [
    path('get_all/', NewApiView.as_view()),
    path('create_comment/', CommentApiView.as_view()),
    path('get_popular_comment/<int:id>', GetCommentPopularApiView.as_view()),
    path('get_all_comment/<int:id>', GetAllCommentInNewApiView.as_view()),
    path('get_like_new/<int:new_id>', GetLikeNewApiView.as_view()),
    path('set_like_new/', SetLikeNewApiView.as_view()),
    path('set_like_comment/', SetLikeCommentApiView.as_view()),
]
