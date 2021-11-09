from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from note.api.serializer import NoteSerializer
from note.models import Notes
from rest_framework.views import APIView
from users.models import CustomUser


class NoteApi(ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)


class CreateNoteApi(CreateAPIView):
    serializer_class = NoteSerializer

    def post(self, request):
        note = Notes.objects.create(user=CustomUser.objects.get(id=request.user.id), title=request.data['title'], text=request.data['text'])
        note.save()
        return Response(NoteSerializer(note).data)


class UpdateNoteApi(APIView):
    def put(self, request):
        note = Notes.objects.get(id=request.data['id'])
        note.text = request.data['text']
        note.title = request.data['title']
        note.save()
        return Response(NoteSerializer(note).data)
    


class CountNoteApi(APIView):
    def get(self, request):
        count = Notes.objects.filter(user=request.user.id).count()
        return Response({'count': count})


class DeleteNoteApi(DestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(NoteSerializer(instance).data)