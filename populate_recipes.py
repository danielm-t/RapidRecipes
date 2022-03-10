import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rapid_recipes.settings')

import django
django.setup()
from recipes.models import Category, Recipe, Ingredient, Instruction
from food.models import RawFood

def populate():

    # Category list
    categories = [
                  {'category': 'starter', 'description': 'A smaller appetizer to wet the palette before the main dish.'},
                  {'category': 'main', 'description': 'The main event, the plat principal, this is star of the show.'},
                  {'category': 'dessert', 'description': "Everyone's favourite part, the desert is the finale to nail the night with."},
                  {'category': 'snack', 'description': "We're all prone to a nibble and nothing quite satisfies this like a snack."},
                  {'category': 'breakfast', 'description': 'The most important mela of the day, nothing quite kicks a day off like a good breakfast.'},
                  {'category': 'lunch', 'description': 'A much needed boost, a good lunch charges you through the day.'},
                  {'category': 'dinner', 'description': 'The highlight of the evening, dinner is the biggest and most satisfying meal of the day.'},
                  {'category': 'drink', 'description': 'From healthy to happy, nothing beats a good drink.'},
                  {'category': 'soup', 'description': 'Warm, hearty and tasty, soup is a cornerstone of lunchtime cuisine.'},
                  {'category': 'salad', 'description': 'Easy to make and healthy to eat, salads are an excellent way to supplement a diet.'},
                  {'category': 'vegan', 'description': 'Free from animal products, these recipes are perfect for vegans.'},
                  {'category': 'vegetarian', 'description': 'Free from meat, these recipes are perfect for vegans.'},
                  {'category': 'beef', 'description': 'Juicy, tender and loaded with flavour, these dishes will put you in a good mood.'},
                  {'category': 'chicken', 'description': 'A pillar of many iconic dishes, chicken is the most used and most loved meat out there.'},
                  {'category': 'fish', 'description': 'Fresh, flaky and flavourful, fish is not only healthy but exceedingly tasty.'},
                  {'category': 'easy', 'description': 'Perfect for beginners, these dishes are simple to complete.'},
                  {'category': 'medium', 'description': 'While maybe challenging for beginners, these dishes are achievable for all.'},
                  {'category': 'hard', 'description': 'Free from meat, these recipes are perfect for vegans.'},
                  {'category': 'quick', 'description': "Great when you're in a rush, these recipes can be completed pronto."} ]

    # Ingredient list
    ingredients = [
                   {'rawFood': 'plain flour', 'amount' : '260', 'recipe': 'dutch butter cake'},
                   {'rawFood': 'caster sugar', 'amount' : '250', 'recipe': 'dutch butter cake'},
                   {'rawFood': 'butter', 'amount' : '250', 'recipe': 'dutch butter cake'},
                   {'rawFood': 'vanilla extract', 'amount' : 'a few', 'recipe': 'dutch butter cake'}]
    
    # Recipe list
    recipes = [
               {'name': 'dutch butter cake', 'categories': ['snack','easy'], 'rating': 4.0, 'difficulty': 0.5, 'imagePath': 
               
    # Populate database
    for type in categories:
        c = Category.objects.get_or_create(category=type['category'],
                                           description=type['description'])[0]
        c.save()
    
    for food in ingredients:
        raw_food = RawFood.objects.get(name=food['rawFood'])
        plan = Recipe.objects.get(name=food['recipe'])
        i = Ingredient.objects.get_or_create(amount=food['amount'])[0]
        i.save()
        i.rawFood.add(raw_food)
        i.recipe.add(plan)