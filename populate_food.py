import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rapid_recipes.settings')

import django
django.setup()
from food.models import Measurement, RawFood

def populate():
    
    # Measurement list
    measurements = [
                    {'type': 'Weight', 'unit': 'gram', 'shorthand': 'g', 'alternative': None},
                    {'type': 'Weight', 'unit': 'kilogram', 'shorthand': 'kg', 'alternative': 'KG'},
                    {'type': 'Volume', 'unit': 'tablespoon', 'shorthand': 'tbsp',  'alternative': 'tbsp.'},
                    {'type': 'Volume', 'unit': 'teaspoon', 'shorthand': 'tsp', 'alternative': 'tsp.'},
                    {'type': 'Weight', 'unit': 'pound', 'shorthand': 'lb', 'alternative': None},
                    {'type': 'Volume', 'unit': 'litre', 'shorthand': 'L', 'alternative': 'ltr'},
                    {'type': 'Volume', 'unit': 'millilitre', 'shorthand': 'ml', 'alternative': None},
                    {'type': 'Volume', 'unit': 'bag', 'shorthand': 'bag', 'alternative': None},
                    {'type': 'Volume', 'unit': 'bar', 'shorthand': 'bar', 'alternative': None},
                    {'type': 'Volume', 'unit': 'bulb', 'shorthand': 'bulb', 'alternative': None},
                    {'type': 'Volume', 'unit': 'capsule', 'shorthand': 'capsule', 'alternative': None},
                    {'type': 'Volume', 'unit': 'clove', 'shorthand': 'clove', 'alternative': None},
                    {'type': 'Volume', 'unit': 'cob', 'shorthand': 'cob', 'alternative': None},
                    {'type': 'Volume', 'unit': 'dash', 'shorthand': 'dash', 'alternative': None},
                    {'type': 'Volume', 'unit': 'drop', 'shorthand': 'drop', 'alternative': None},
                    {'type': 'Volume', 'unit': 'head', 'shorthand': 'head', 'alternative': None},
                    {'type': 'Volume', 'unit': 'leaf', 'shorthand': 'leaf', 'alternative': None},
                    {'type': 'Volume', 'unit': 'loaf', 'shorthand': 'loaf', 'alternative': None},
                    {'type': 'Volume', 'unit': 'package', 'shorthand': 'pack', 'alternative': None},
                    {'type': 'Volume', 'unit': 'pinch', 'shorthand': 'pinch', 'alternative': None},
                    {'type': 'Volume', 'unit': 'scoop', 'shorthand': 'scoop', 'alternative': None},
                    {'type': 'Volume', 'unit': 'sheet', 'shorthand': 'sheet', 'alternative': None},
                    {'type': 'Volume', 'unit': 'slice', 'shorthand': 'slice', 'alternative': None},
                    {'type': 'Volume', 'unit': 'sprig', 'shorthand': 'sprig', 'alternative': None},
                    {'type': 'Volume', 'unit': 'stalk', 'shorthand': 'stalk', 'alternative': None},
                    {'type': 'Volume', 'unit': 'strip', 'shorthand': 'strip', 'alternative': None},
                    {'type': 'Volume', 'unit': 'teabag', 'shorthand': 'teabag', 'alternative': None} ]
    
    # Raw food list
    raw_foods = [
                {'name': 'plain flour', 'measuredIn': 'gram'},
                {'name': 'caster sugar', 'measuredIn': 'gram'},
                {'name': 'butter', 'measuredIn': 'gram'},
                {'name': 'vanilla extract', 'measuredIn': 'drop'} ]
    
    # Populate database
    for measurement in measurements:
        if measurement['alternative'] == None:
            m = Measurement.objects.get_or_create(type=measurement['type'], unit=measurement['unit'], 
                                          shorthand=measurement['shorthand'])[0]
            
        else:
            m = Measurement.objects.get_or_create(type=measurement['type'], unit=measurement['unit'], 
                                          shorthand=measurement['shorthand'], alternative=measurement['alternative'])[0]
        m.save()
    
    
    for raw_food in raw_foods:
        measurement = Measurement.objects.get(unit=raw_food['measuredIn'])
        r = RawFood.objects.get_or_create(name=raw_food['name'])[0]
        r.save()
        r.measuredIn.add(measurement)
    


        
def add_measurement(type, unit, shorthand, alternative):
    Measurement.objects.get_or_create(type=type,unit=unit,shorthand=shorthand, alternative=alternative)

# Start execution here
if __name__ == '__main__':
    print('Starting food population script...')
    populate()