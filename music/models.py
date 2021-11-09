from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Type(models.Model):
    title = models.CharField(max_length=20)


class Music(models.Model):
    title = models.CharField(max_length=100)
    music = models.FileField()
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE, null=True, blank=True)
    year = models.IntegerField(validators=[MaxValueValidator(2021), MinValueValidator(1950)])
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + str(self.id)


class FavoriteMusic(models.Model):
    # создается новый экземпляр при регистрации нового пользователя
    music = models.ManyToManyField(Music, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Playlist(models.Model):
    title = models.CharField(max_length=30)
    # music = models.ManyToManyField(Music, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + str(self.id)
