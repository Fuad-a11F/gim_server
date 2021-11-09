from django.db import models
from django.conf import settings


class Notes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
