from django.contrib import admin
from .models import *

class AllTicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'price', 'withCoach')

admin.site.register(AllTickets, AllTicketsAdmin)
admin.site.register(UserTicket)
admin.site.register(Review)
admin.site.register(ProgramTraining)
admin.site.register(Draft)
admin.site.register(Rating)
admin.site.register(ProgramTrainingItem)



