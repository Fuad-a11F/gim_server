from django.db import models
from django.conf import settings


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    new = models.ForeignKey('New', on_delete=models.CASCADE, blank=True, null=True)


class New(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class LikeNew(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class LikeComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
