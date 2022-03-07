import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rapid_recipes.settings')

import django
django.setup()
from food.models import GroceryItem, UserProfile

def populate():
    
    