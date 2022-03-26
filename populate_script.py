import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rapid_recipes.settings')

import django
django.setup()
import populate_food, populate_recipes, populate_groceries

# Start execution here
if __name__ == '__main__':
    print('Starting population script...')
    print('Starting food population script...')
    populate_food.populate()
    print('Starting recipes population script...')
    populate_recipes.populate()
    print('Starting groceries population script...')
    populate_groceries.populate()
    print("Done!")