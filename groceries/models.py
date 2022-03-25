from django.db import models
from django.contrib.auth.models import User
from food.models import RawFood, Measurement
from recipes.models import Recipe

class GroceryItem(models.Model):

    AMOUNT_MAX_LENGTH = 50

    rawFood = models.ForeignKey(RawFood, on_delete=models.CASCADE)
    amount = models.CharField(max_length=AMOUNT_MAX_LENGTH)
    available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    measuredIn = models.ForeignKey(Measurement, on_delete=models.CASCADE)

    def __str__(self):
        return self.rawFood.name
