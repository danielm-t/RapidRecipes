import importlib
from food.models import Measurement, RawFood
from django.test import TestCase
from food.urls import *
from django.test import Client
from django.urls import reverse
from django.core import serializers

# Create your tests here.


def CreateMeasurement():
    measurement = Measurement.objects.get_or_create(type='Temperature', unit='Kilogram', shorthand='Kg', alternative='KG.')

    return measurement

def CreateRawFood():
    rawfood = RawFood.objects.get_or_create(name='Chicken')
    rawfood.measuredIn.add(CreateMeasurement())

    return rawfood

