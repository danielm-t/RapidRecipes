import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rapid_recipes.settings')

import django
django.setup()
from recipes.models import Category, Recipe, Ingredient, Instruction
from food.models import RawFood
from rapid_recipes.settings import MEDIA_ROOT

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
                  {'category': 'hard', 'description': 'A challenge for all, these dishes will realy test your metal.'},
                  {'category': 'quick', 'description': "Great when you're in a rush, these recipes can be completed pronto."} ]

    # Ingredient list
    ingredients = [
                   {'rawFood': 'plain flour', 'amount' : '260', 'recipe': 'dutch butter cake'},
                   {'rawFood': 'caster sugar', 'amount' : '250', 'recipe': 'dutch butter cake'},
                   {'rawFood': 'butter', 'amount' : '250', 'recipe': 'dutch butter cake'},
                   {'rawFood': 'vanilla extract', 'amount' : 'a few', 'recipe': 'dutch butter cake'},
                   {'rawFood': 'butter', 'amount' : '50', 'recipe': 'Burger'},
                   {'rawFood': 'lettuce', 'amount' : 'a couple', 'recipe': 'Burger'},
                   {'rawFood': 'tomato', 'amount' : 'a couple', 'recipe': 'Burger'},
                   {'rawFood': 'beef burger', 'amount' : '200', 'recipe': 'Burger'},
                   {'rawFood': 'bread', 'amount' : '1', 'recipe': 'Burger'},]

    # Recipe list
    recipes = [
               {'name': 'dutch butter cake', 'categories': ['snack','easy'], 'rating': 4.0,
                'difficulty': 0.5, 'imagePath': 'dutch_butter_cake.png'},
               {'name': 'Burger', 'categories': ['dessert','medium'], 'rating': 0.0,
                'difficulty': 2.0, 'imagePath': 'borgor.png'},
               {'name': 'Curry', 'categories': ['lunch','hard'], 'rating': 5.0,
                'difficulty': 5.0, 'imagePath': 'mix.jpg'}]

    # Instruction list
    instructions = [
                    {'step': 0, 'recipe': 'dutch butter cake', 'media': None, 'description': 'Preheat oven to gas 3 (140 degrees Celsius).'},
                    {'step': 1, 'recipe': 'dutch butter cake', 'media': None, 'description': 'Grease a shallow cake tin of about 20-22 cm diameter with a little butter. It is very helpful if your tin has slanted edges.'},
                    {'step': 2, 'recipe': 'dutch butter cake', 'media': None, 'description': 'Mix the flour, sugar, butter and vanilla essence and knead into a supple ball of dough in a large mixing bowl. It may help to cut the butter into small pieces with two knives first, before mixing with your hands. '},
                    {'step': 3, 'recipe': 'dutch butter cake', 'media': None, 'description': 'Press the dough into the form, making sure there is slightly more dough peripherally, to avoid the edge from overcooking.'},
                    {'step': 4, 'recipe': 'dutch butter cake', 'media': None, 'description': 'Place on a high shelf and check after about 35 minutes. Only check by eye, it should look slightly underdone, if it is browning then it is probably too far gone as the edge will set rock-hard when it cools. It should look like raw dough in the middle but nowhere should be darker than golden buttery yellow.'},
                    {'step': 5, 'recipe': 'dutch butter cake', 'media': None, 'description': 'Take the tin from the oven- it is okay if it looks very fluid as this will set when cooling. Cut into diamonds of about 3 x 3 cms, as the pieces are very calorific. Cut the cake when it is lukewarm, that is easier than when it is completely cold.'},
                    {'step': 0, 'recipe': 'Burger', 'media': None, 'description': 'Preheat the oven to what is needed for you beef burgers.'},
                    {'step': 1, 'recipe': 'Burger', 'media': None, 'description': 'When the oven is at the appropriate temperature, put the burger buns in for the time specified for them.'},
                    {'step': 2, 'recipe': 'Burger', 'media': None, 'description': 'Slice your tomato and lettuce leaves to what you want and butter your buns.'},
                    {'step': 0, 'recipe': 'Burger', 'media': None, 'description': 'Build your burger in the manner that you want.'}]


    # Populate database
    for type in categories:
        c = Category.objects.get_or_create(category=type['category'],
                                           description=type['description'])[0]
        c.save()

    for plan in recipes:
        r = Recipe.objects.get_or_create(name=plan['name'],
                                         rating=plan['rating'],
                                         difficulty=plan['difficulty'],
                                         imagePath=plan['imagePath'])[0]
        r.save()
        for cat in plan['categories']:
            category = Category.objects.get(category=cat)
            r.category.add(category)

    for food in ingredients:
        raw_food = RawFood.objects.get(name=food['rawFood'])
        plan = Recipe.objects.get(name=food['recipe'])
        i = Ingredient.objects.get_or_create(amount=food['amount'], rawFood=raw_food, recipe=plan)[0]
        i.save()

    for instruction in instructions:
        plan = Recipe.objects.get(name=instruction['recipe'])
        if instruction['media'] != None:
            i = Instruction.objects.get_or_create(step=instruction['step'],
                                                  description=instruction['description'],
                                                  media=instruction['media'],
                                                  recipe=plan)[0]
        else:
            i = Instruction.objects.get_or_create(step=instruction['step'],
                                                  description=instruction['description'],
                                                  recipe=plan)[0]
        i.save()

# Start execution here
if __name__ == '__main__':
    print('Starting recipes population script...')
    populate()
