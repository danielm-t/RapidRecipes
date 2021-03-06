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
                    {'type': 'Volume', 'unit': 'bun', 'shorthand': 'bun', 'alternative': None},
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
                    {'type': 'Volume', 'unit': 'stem', 'shorthand': 'stem', 'alternative': None},
                    {'type': 'Volume', 'unit': 'strip', 'shorthand': 'strip', 'alternative': None},
                    {'type': 'Volume', 'unit': 'teabag', 'shorthand': 'teabag', 'alternative': None},
                    {'type': 'Volume', 'unit': 'blank', 'shorthand': '', 'alternative': None}]
    
    # Raw food list
    raw_foods = [
                {'name': 'plain flour', 'measuredIn': ['gram']},
                {'name': 'caster sugar', 'measuredIn': ['gram']},
                {'name': 'butter', 'measuredIn': ['gram']},
                {'name': 'vanilla extract', 'measuredIn': ['drop']},
                {'name': 'bread bun', 'measuredIn': ['blank']},
                {'name': 'beef burger', 'measuredIn': ['gram']},
                {'name': 'lettuce', 'measuredIn': ['leaf']},
                {'name': 'tomato', 'measuredIn': ['blank']},
                {'name': 'onion', 'measuredIn': ['blank']},
                {'name': 'vegetable oil', 'measuredIn': ['tablespoon']},
                {'name': 'curry paste', 'measuredIn': ['millilitre']},
                {'name': 'red lentils', 'measuredIn': ['gram']},
                {'name': 'tinned tomato', 'measuredIn': ['gram']},
                {'name': 'vegetable stock', 'measuredIn': ['millilitre']},
                {'name': 'strong flour', 'measuredIn': ['gram']},
                {'name': 'yeast', 'measuredIn': ['gram']},
                {'name': 'olive oil', 'measuredIn': ['tablespoon']},
                {'name': 'tomato sauce', 'measuredIn': ['millilitre']},
                {'name': 'cheese', 'measuredIn': ['gram']},
                {'name': 'big potato', 'measuredIn': ['blank']},
                {'name': 'courgette', 'measuredIn': ['blank']},
                {'name': 'aubergine', 'measuredIn': ['blank']},
                {'name': 'pepper', 'measuredIn': ['blank']},
                {'name': 'feta', 'measuredIn': ['gram']},
                {'name': 'baked beans', 'measuredIn': ['gram']},
                {'name': 'milk', 'measuredIn': ['millilitre']},
                {'name': 'carrot', 'measuredIn': ['blank']},
                {'name': 'macaroni pasta', 'measuredIn': ['gram']},
                {'name': 'mince', 'measuredIn': ['gram']},
                {'name': 'black beans', 'measuredIn': ['gram']},
                {'name': 'smoked paprika', 'measuredIn': ['dash']},
                {'name': 'bean sprouts', 'measuredIn': ['gram']},
                {'name': 'peas', 'measuredIn': ['gram']},
                {'name': 'ginger', 'measuredIn': ['stem']},
                {'name': 'stir fry sauce', 'measuredIn': ['millilitre']},
                {'name': 'noodles', 'measuredIn': ['gram']},
                {'name': 'double cream', 'measuredIn': ['millilitre']},
                {'name': 'dark chocolate', 'measuredIn': ['gram']},
                {'name': 'egg', 'measuredIn': ['blank']},
                {'name': 'chocolate chips', 'measuredIn': ['gram']},
                {'name': 'rolled oats', 'measuredIn': ['gram']},
                {'name': 'apple', 'measuredIn': ['gram']},
                {'name': 'ground almonds', 'measuredIn': ['gram']},
                {'name': 'chocolate', 'measuredIn': ['gram']},
                {'name': 'baking powder', 'measuredIn': ['teaspoon']}]

    
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
        r = RawFood.objects.get_or_create(name=raw_food['name'])[0]
        r.save()
        for measurementType in raw_food['measuredIn']:
            measurement = Measurement.objects.get(unit=measurementType)
            r.measuredIn.add(measurement)
    


        
def add_measurement(type, unit, shorthand, alternative):
    Measurement.objects.get_or_create(type=type,unit=unit,shorthand=shorthand, alternative=alternative)

# Start execution here
if __name__ == '__main__':
    print('Starting food population script...')
    populate()