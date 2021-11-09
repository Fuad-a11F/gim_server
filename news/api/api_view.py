from django.db.models.query_utils import Q
from rest_framework.response import Response
from django.db.models import Count
from ..models import LikeComment, LikeNew, New, Comment
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializer import  CommentAllSerializer, CommentPagination, NewSerializer, CommentCreateSerializer, CommentSerializer, PopularCommentSerializer


class NewApiView(APIView):
    def get(self, request):
        queryset = New.objects.all().annotate(commentCount=Count('comment'))
        serializer = NewSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentApiView(CreateAPIView):
    serializer_class = CommentCreateSerializer

    def post(self, request):
        comment = Comment.objects.create(new=New.objects.get(id=request.data['new']), text=request.data['text'], user=request.user)
        comment.save()
        return Response('ok')


class GetCommentPopularApiView(APIView):
    def get(self, request, id):
        popular = Comment.objects.filter(new=id).annotate(likeCount=Count('likecomment'), isLike=Count('likecomment', filter=Q(likecomment__user=request.user.id))).order_by('-likeCount').first()
        
        return Response(PopularCommentSerializer(popular, context={'request': request}).data)


class GetLikeNewApiView(APIView):
    def get(self, request, new_id):
        popular = LikeNew.objects.filter(new=new_id).count()
        check_like = LikeNew.objects.filter(new=new_id, user=request.user.id).count()
        return Response({'count': popular, 'isLike': True if check_like > 0 else False})


class GetLikeCommentApiView(APIView):
    def get(self, request, new_id):
        popular = LikeComment.objects.filter(new=new_id).count()
        check_like = LikeComment.objects.filter(new=new_id, user=request.user.id).count()
        return Response({'count': popular, 'isLike': True if check_like > 0 else False})


class SetLikeNewApiView(APIView):
    def post(self, request):
        check_like = LikeNew.objects.filter(new=request.data.get('new_id'), user=request.user.id)
        if len(check_like) == 0:
            like = LikeNew.objects.create(new=New.objects.get(id=request.data.get('new_id')), user=request.user)
            return Response({'result': 'Лайк поставлен', 'id': like.id})
        like_del = check_like[0].id
        check_like.delete()
        return Response({'result': 'Лайк удален', 'id': like_del})


class SetLikeCommentApiView(APIView):
    def post(self, request):
        check_like = LikeComment.objects.filter(comment=request.data.get('comment_id'), user=request.user.id)
        if len(check_like) == 0:
            like = LikeComment.objects.create(comment=Comment.objects.get(id=request.data.get('comment_id')), user=request.user)
            return Response({'result': 'Лайк поставлен', 'id': like.id})
        like_del = check_like[0].id
        check_like.delete()
        return Response({'result': 'Лайк удален', 'id': like_del})


class GetAllCommentInNewApiView(ListAPIView):
    serializer_class = CommentAllSerializer
    pagination_class = CommentPagination

    def get_queryset(self):
        return Comment.objects.filter(new=self.kwargs['id']).annotate(likeCount=Count('likecomment'), isLike=Count('likecomment', filter=Q(likecomment__user=self.request.user)))   



        