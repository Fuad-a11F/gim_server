from django.conf import settings
from django.db import models

CLUB = [
    ('eat', 'eat'),
    ('drink', 'drink')
]

class Food(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(choices=CLUB, max_length=10)
    proteins = models.IntegerField()
    fats = models.IntegerField()
    carbohydrates = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title


class ProgramFood(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='userF', on_delete=models.CASCADE)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    text = models.CharField(max_length=200)
    isNew = models.BooleanField(default=True)
    isActive = models.BooleanField(default=False)
    foodItems = models.ManyToManyField('FoodTrainingItem')


class FoodTrainingItem(models.Model):
    number = models.IntegerField()
    text = models.TextField()


class DraftFood(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='userDF', on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    foodItems = models.ManyToManyField('FoodTrainingItem')