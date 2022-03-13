import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rapid_recipes.settings')

import django
django.setup()
from django.contrib.auth.models import User
from groceries.models import GroceryItem, UserProfile
from food.models import RawFood

def populate():
    
    # GroceryItem list
    items = [
             {'rawFood': 'caster sugar', 'amount': '250', 'available': True, 'user': 'Bob'},
             {'rawFood': 'plain flour', 'amount': '260', 'available': False, 'user': 'Bob'},
             {'rawFood': 'butter', 'amount': '250', 'available': True, 'user': 'Bob'},
             {'rawFood': 'vanilla extract', 'amount': 'a few', 'available': False, 'user': 'Bob'},
             {'rawFood': 'butter', 'amount': '50', 'available': True, 'user': 'Jill'},
             {'rawFood': 'bread', 'amount': '1', 'available': True, 'user': 'Jill'},
             {'rawFood': 'lettuce', 'amount': 'a couple', 'available': False, 'user': 'Jill'},
             {'rawFood': 'tomato', 'amount': 'a couple', 'available': True, 'user': 'Jill'},
             {'rawFood': 'beef burger', 'amount': '200', 'available': False, 'user': 'Jill'}]
    
    # UserProfile list
    users = [
             {'user': 'Bob', 'email': 'bobsyouruncle@gmail.com', 'password': 'BobbingAround'},
             {'user': 'Jill', 'email': 'justjilling@gmail.com', 'password': 'EatYourJill'}]
    
    # populate database
    for person in users:
        u = User.objects.get_or_create(email=person['email'],
                                       password=person['password'],
                                       username=person['user'])[0]
        
        name = User.objects.get(username=person['user'])
        p = UserProfile.objects.get_or_create(email=person['email'],
                                              password=person['password'],
                                              user=name)[0]
        p.save()
    
    for food in items:
        raw_food = RawFood.objects.get(name=food['rawFood'])
        name = User.objects.get(username=food['user'])
        g = GroceryItem.objects.get_or_create(amount=food['amount'],
                                              available=food['available'],
                                              user=name,
                                              rawFood=raw_food)[0]
        g.save()
        
# Start execution here
if __name__ == '__main__':
    print('Starting groceries population script...')
    populate()