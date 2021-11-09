from rest_framework.response import Response
from gim.api.serializer import *
from gim.models import AllTickets, Draft, ProgramTraining, ProgramTrainingItem, UserTicket
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from django.conf import settings
from users.models import CustomUser
import datetime

class TicketCheckApi(APIView):
    def get(self, request):
        try:
            ticket = UserTicket.objects.get(user=request.user, active=True)
            serializer = TicketSerializer(ticket)
            return Response(serializer.data)
        except:
            return Response({'result': False})


class CustomUserNameApi(ListAPIView):
    queryset = CustomUser.objects.filter(position='student')
    serializer_class = UserNameSerializer


class CustomOneUserNameApi(ListAPIView):
    serializer_class = UserNameSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

class ProgramTrainingApi(ListAPIView):
    serializer_class = ProgramTrainingSerializer

    def get_queryset(self):
        return ProgramTraining.objects.filter(user_to=self.request.user.id, new_type__in=['New', 'During']).order_by('new_type')


class ProgramTrainingOldApi(ListAPIView):
    serializer_class = ProgramTrainingSerializer

    def get_queryset(self):
        return ProgramTraining.objects.filter(user_to=self.request.user.id, new_type='Old')


class DraftApi(ListAPIView):
    serializer_class = DraftSerializer

    def get_queryset(self):
        return Draft.objects.filter(user=self.request.user.id)


class ProgramTrainingItemApi(ListAPIView):
    serializer_class = ProgramTrainingItemSerializer

    def get_queryset(self):
        return ProgramTraining.objects.filter(pk=self.kwargs['id'])


class ProgramTrainingCreateApi(APIView):
    def post(self, request):
        items = []
        for item in request.data.get('items'):
            items += [ProgramTrainingItem.objects.create(**item)]

        if request.data.get('action') == 'Отправить':
            program = ProgramTraining.objects.create(date = request.data.get('date'), 
                                            user = request.user,
                                            user_to = CustomUser.objects.get(pk=request.data.get('user_to')),
                                            text = request.data.get('text'))

        elif request.data.get('action') == 'Сохранить':
            program = Draft.objects.create(date = request.data.get('date'), 
                                            user = request.user,
                                            text = request.data.get('text'))

        elif request.data.get('action') == 'Отправить и сохранить':
            program1 = ProgramTraining.objects.create(date = request.data.get('date'), 
                                            user = request.user,
                                            user_to = CustomUser.objects.get(pk=request.data.get('user_to')),
                                            text = request.data.get('text'))

            program2 = Draft.objects.create(date = request.data.get('date'), 
                                            user = request.user,
                                            text = request.data.get('text'))
            
            for item in items:
                program1.programItems.add(item)
                program2.programItems.add(item)
            
            return Response({'success': 'Запись успешно сохранена и отправлена'})


        for item in items:
            program.programItems.add(item)

        return Response({'success': 'Запись успешно отправлена'})


class CoachApi(APIView):
    def get(self, request):
        user = CustomUser.objects.filter(position='coach')
        serializer = CoachSerializer(user, many=True)
        return Response(serializer.data)


# class CoachApi(ListAPIView):
#     serializer_class = CoachSerializer

#     def get_queryset(self):
#         return CustomUser.objects.filter(position='coach')


class CoachDetailApi(APIView):
    def get(self, request, id):
        coach = CustomUser.objects.get(id=id)
        serializer = CoachDetailSerializer(coach)
        return Response(serializer.data)


class GetPriceTicket(APIView):
    def get(self, request):
        finish_time = ''
        if (request.GET.get('period') == 'day'): finish_time = 1 
        elif (request.GET.get('period') == 'week'): finish_time = 7 
        elif (request.GET.get('period') == 'month'): finish_time = 30 
        elif (request.GET.get('period') == 'year'): finish_time = 365
        ticket = AllTickets.objects.filter(withCoach=True if request.GET.get('coach') == 'true' else False)
        ticket_price = ticket.get(finish_time=finish_time).price
        ticket_id = ticket.get(finish_time=finish_time).id
        return Response({'price': ticket_price, 'id': ticket_id})
        


class CreateTicketForUser(APIView):
    def post(self, request):
        user_ticket = UserTicket.objects.create(user = request.user,
                                    buy_time = request.data['start_time'],
                                    finish_time = request.data['finish_time'],
                                    coach = CustomUser.objects.get(id=request.data['coach']),
                                    alltickets = AllTickets.objects.get(id=request.data['whom_id']))
        user_ticket.save()
        return Response('ok')


class ProgramItemDoneTrainingApi(APIView):
    def put(self, request, id):
        done = ProgramTrainingItem.objects.get(id=id)
        done.done = True
        done.save()
        return Response('ok')


class BeginTrainApi(APIView):
    def put(self, request, id):
        program = ProgramTraining.objects.get(id=id)
        program.beginAt = datetime.datetime.now()
        program.new_type = 'During'
        program.save()
        return Response('ok')


class FinishTrainApi(APIView):
    def put(self, request, id):
        program = ProgramTraining.objects.get(id=id)
        program.finishAt = datetime.datetime.now()
        program.new_type = 'Old'
        program.save()
        return Response('ok')


class GetProgramLastApi(APIView):
    def get(self, request):
        program = ProgramTraining.objects.order_by('time').filter(user_to=request.user.id, new_type__in=('New', 'During')).first()
        return Response(ProgramTrainingSerializer(program).data)


class AbonementCountApi(APIView):
    def get(self, request):
        abonement_count = UserTicket.objects.filter(user=request.user).count()
        return Response(abonement_count)


class GetAbonementsApi(ListAPIView):
    serializer_class = TicketSerializer

    def get_queryset(self):
        return UserTicket.objects.filter(user=self.request.user).order_by('-id')
        




