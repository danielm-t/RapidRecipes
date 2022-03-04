from django.db import models

class Measurement(models.Model):

    TYPE_MAX_LENGTH = 128
    UNIT_MAX_LENGTH = 128
    SHORTHAND_MAX_LENGTH = 128
    ALTERNATIVE_MAX_LENGTH = 255

    class Type(models.TextChoices):
        TEMPERATURE = 'Temperature'
        WEIGHT = 'Weight'
        TIME = 'Time'
        LENGTH = 'Length'
        VOLUME = 'Volume'
    
    type = models.CharField(max_length=TYPE_MAX_LENGTH, choices = Type.choices)
    # Name of the unit (Kilogram...)
    unit = models.CharField(max_length=UNIT_MAX_LENGTH, unique=True)
    # Shorthand notation (Kg)
    shorthand = models.CharField(max_length=SHORTHAND_MAX_LENGTH)
    # Alternative notation (KG.)
    alternative = models.CharField(max_length=ALTERNATIVE_MAX_LENGTH, blank=True)

    
class RawFood(models.Model):
    
    NAME_MAX_LENGTH = 255
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    measuredIn = models.ManyToManyField(Measurement)

    def __str__(self):
        return self.name


