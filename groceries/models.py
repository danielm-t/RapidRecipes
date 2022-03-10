from django.db import models
from django.contrib.auth.models import User
from food.models import RawFood

class GroceryItem(models.Model):

    AMOUNT_MAX_LENGTH = 50

    rawFood = models.ForeignKey(RawFood, on_delete=models.CASCADE)
    amount = models.CharField(max_length=AMOUNT_MAX_LENGTH)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rawFood.name

class UserProfile(models.Model):

    EMAIL_MAX_LENGTH = 255
    PASSWORD_MAX_LENGTH = 255

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.CharField(max_length=EMAIL_MAX_LENGTH)
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH)

    def __str__(self):
        return self.user.username
