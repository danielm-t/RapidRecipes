import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rapid_recipes.settings')

import django
django.setup()
from django.contrib.auth.models import User
from groceries.models import GroceryItem
from food.models import RawFood, Measurement

def populate():
    
    # GroceryItem list
    items = [
             {'rawFood': 'caster sugar', 'amount': '250', 'available': True, 'user': 'Bob', 'unit':'gram'},
             {'rawFood': 'plain flour', 'amount': '260', 'available': False, 'user': 'Bob', 'unit':'gram'},
             {'rawFood': 'butter', 'amount': '250', 'available': True, 'user': 'Bob', 'unit':'gram'},
             {'rawFood': 'vanilla extract', 'amount': 'a few', 'available': False, 'user': 'Bob', 'unit':'drop'},
             {'rawFood': 'butter', 'amount': '50', 'available': True, 'user': 'Jill', 'unit':'gram'},
             {'rawFood': 'bread bun', 'amount': '1', 'available': True, 'user': 'Jill', 'unit':'blank'},
             {'rawFood': 'lettuce', 'amount': 'a couple', 'available': False, 'user': 'Jill', 'unit':'leaf'},
             {'rawFood': 'tomato', 'amount': 'a couple', 'available': True, 'user': 'Jill', 'unit':'slice'},
             {'rawFood': 'beef burger', 'amount': '200', 'available': False, 'user': 'Jill', 'unit':'gram'}]
    
    # UserProfile list
    users = [
             {'user': 'Bob', 'email': 'bobsyouruncle@gmail.com', 'password': 'BobbingAround'},
             {'user': 'Jill', 'email': 'justjilling@gmail.com', 'password': 'EatYourJill'}]
    
    # populate database
    for person in users:
        u = User.objects.create_user(email=person['email'],
                                    password=person['password'],
                                    username=person['user'])
    
    for food in items:
        raw_food = RawFood.objects.get(name=food['rawFood'])
        name = User.objects.get(username=food['user'])
        measurement = Measurement.objects.get(unit=food['unit'])
        g = GroceryItem.objects.get_or_create(amount=food['amount'],
                                              available=food['available'],
                                              user=name,
                                              rawFood=raw_food,
                                              measuredIn=measurement)[0]
        g.save()
        
# Start execution here
if __name__ == '__main__':
    print('Starting groceries population script...')
    populate()