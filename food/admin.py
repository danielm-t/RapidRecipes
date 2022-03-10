from django.contrib import admin
from food.models import Measurement, RawFood


# Register your models here.
admin.site.register(Measurement)
admin.site.register(RawFood)