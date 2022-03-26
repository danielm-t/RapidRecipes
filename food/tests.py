from food.models import Measurement, RawFood

# Create your tests here.


def CreateMeasurement():
    measurement = Measurement.objects.get_or_create(type='Temperature', unit='Kilogram', shorthand='Kg', alternative='KG.')

    return measurement

def CreateRawFood():
    rawfood = RawFood.objects.get_or_create(name='Chicken')
    rawfood.measuredIn.add(CreateMeasurement())

    return rawfood

