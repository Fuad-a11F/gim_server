from django.db import models
from django.conf import settings

RATING = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
]

FINISH_TIME = [
    (1, 1),
    (7, 7),
    (30, 30),
    (365, 365)
]

class AllTickets(models.Model):
    finish_time = models.IntegerField(choices=FINISH_TIME, verbose_name='Период')
    description = models.CharField(max_length=100, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    withCoach = models.BooleanField(verbose_name='С тренером ли?')

    class Meta:
        verbose_name = 'Все билеты'
        verbose_name_plural = 'Все билеты'


class UserTicket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    alltickets = models.ForeignKey(AllTickets, on_delete=models.CASCADE)
    buy_time = models.DateField(null=True, blank=True)
    finish_time = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    coach = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='trainer', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Билет пользователя'
        verbose_name_plural = 'Билеты пользователя'


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='userR', on_delete=models.CASCADE)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()


class Rating(models.Model):
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING)


class ProgramTraining(models.Model):
    date = models.DateField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='userT', on_delete=models.CASCADE)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    new_type = models.CharField(default='New', max_length=20)
    beginAt = models.DateTimeField(null=True, blank=True)
    finishAt = models.DateTimeField(null=True, blank=True)
    programItems = models.ManyToManyField('ProgramTrainingItem')


class ProgramTrainingItem(models.Model):
    number = models.IntegerField()
    text = models.TextField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    done = models.BooleanField(default=False)


class Draft(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='userD', on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    programItems = models.ManyToManyField('ProgramTrainingItem')
