from django.db import models
from django.conf import settings


class Friend(models.Model):
    me = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='my_friend', on_delete=models.CASCADE)
    friends = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_friend = models.BooleanField(default=False)


