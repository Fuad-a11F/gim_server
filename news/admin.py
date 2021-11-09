from django.contrib import admin
from .models import *

admin.site.register(Comment)
admin.site.register(New)
admin.site.register(LikeNew)
admin.site.register(LikeComment)
