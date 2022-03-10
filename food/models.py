from django.db import models
from enum import Enum

class Measurement(models.Model):

    TYPE_MAX_LENGTH = 128
    UNIT_MAX_LENGTH = 128
    SHORTHAND_MAX_LENGTH = 128
    ALTERNATIVE_MAX_LENGTH = 255

    class Type(Enum): # Enum for Django version < 3: https://stackoverflow.com/questions/54802616/how-to-use-enums-as-a-choice-field-in-django-model
        TEMPERATURE = 'Temperature'
        WEIGHT = 'Weight'
        TIME = 'Time'
        LENGTH = 'Length'
        VOLUME = 'Volume'

        @classmethod
        def choices(cls):
            return tuple((i.name, i.value) for i in cls)
    
    type = models.CharField(max_length=TYPE_MAX_LENGTH, choices = Type.choices())
    # Name of the unit (Kilogram...)
    unit = models.CharField(max_length=UNIT_MAX_LENGTH, unique=True)
    # Shorthand notation (Kg)
    shorthand = models.CharField(max_length=SHORTHAND_MAX_LENGTH)
    # Alternative notation (KG.)
    alternative = models.CharField(max_length=ALTERNATIVE_MAX_LENGTH, blank=True)

    def __str__(self):
        return self.shorthand

    
class RawFood(models.Model):
    
    NAME_MAX_LENGTH = 255
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    measuredIn = models.ManyToManyField(Measurement)

    def __str__(self):
        return self.name


