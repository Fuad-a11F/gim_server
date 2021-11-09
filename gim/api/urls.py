from gim.api.api_view import *
from django.urls import path

urlpatterns = [
    path('check_user/', TicketCheckApi.as_view()),
    path('get_name_user/', CustomUserNameApi.as_view()),
    path('get_my_name/', CustomOneUserNameApi.as_view()),
    path('get_program/', ProgramTrainingApi.as_view()),
    path('get_program_old/', ProgramTrainingOldApi.as_view()),
    path('create_program/', ProgramTrainingCreateApi.as_view()),
    path('get_program_item/<int:id>', ProgramTrainingItemApi.as_view()),
    path('get_draft_program/', DraftApi.as_view()),
    path('coaches/', CoachApi.as_view()),
    path('coach/<int:id>', CoachDetailApi.as_view()),
    path('get_price_ticket/', GetPriceTicket.as_view()),
    path('create_ticket/', CreateTicketForUser.as_view()),
    path('set_program_done_program/<int:id>', ProgramItemDoneTrainingApi.as_view()),
    path('begin_train/<int:id>', BeginTrainApi.as_view()),
    path('finish_train/<int:id>', FinishTrainApi.as_view()),
    path('get_last_program/', GetProgramLastApi.as_view()),
    path('abonement_count/', AbonementCountApi.as_view()),
    path('get_abonements/', GetAbonementsApi.as_view()),
]
