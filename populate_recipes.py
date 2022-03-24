import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rapid_recipes.settings')

import django
django.setup()
from recipes.models import Category, Recipe, Ingredient, Instruction
from food.models import RawFood, Measurement
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
                   {'rawFood': 'plain flour', 'amount' : '260', 'recipe': 'Dutch butter cake', 'unit':'gram'},
                   {'rawFood': 'caster sugar', 'amount' : '250', 'recipe': 'Dutch butter cake', 'unit':'gram'},
                   {'rawFood': 'butter', 'amount' : '250', 'recipe': 'Dutch butter cake', 'unit':'gram'},
                   {'rawFood': 'vanilla extract', 'amount' : 'a few', 'recipe': 'Dutch butter cake', 'unit':'drop'},
                   {'rawFood': 'butter', 'amount' : '50', 'recipe': 'Burger', 'unit':'gram'},
                   {'rawFood': 'lettuce', 'amount' : 'a couple', 'recipe': 'Burger', 'unit':'leaf'},
                   {'rawFood': 'tomato', 'amount' : 'a couple', 'recipe': 'Burger', 'unit':'slice'},
                   {'rawFood': 'beef burger', 'amount' : '200', 'recipe': 'Burger', 'unit':'gram'},
                   {'rawFood': 'bread', 'amount' : '1', 'recipe': 'Burger', 'unit':'bun'},
                   {'rawFood': 'onion', 'amount' : '1', 'recipe': 'Dahl curry', 'unit':'blank'},
                   {'rawFood': 'vegetable oil', 'amount' : '1', 'recipe': 'Dahl curry', 'unit':'tablespoon'},
                   {'rawFood': 'curry paste', 'amount' : '50', 'recipe': 'Dahl curry', 'unit':'millilitre'},
                   {'rawFood': 'red lentils', 'amount' : '200', 'recipe': 'Dahl curry', 'unit':'gram'},
                   {'rawFood': 'tinned tomato', 'amount' : '400', 'recipe': 'Dahl curry', 'unit':'gram'},
                   {'rawFood': 'vegetable stock', 'amount' : '200', 'recipe': 'Dahl curry', 'unit':'millilitre'},
                   {'rawFood': 'yeast', 'amount' : '7', 'recipe': 'Pizza', 'unit':'gram'},
                   {'rawFood': 'olive oil', 'amount' : '1', 'recipe': 'Pizza', 'unit':'tablespoon'},
                   {'rawFood': 'tomato sauce', 'amount' : '100', 'recipe': 'Pizza', 'unit':'millilitre'},
                   {'rawFood': 'cheese', 'amount' : '200', 'recipe': 'Pizza', 'unit':'gram'},
                   {'rawFood': 'onion', 'amount' : '1', 'recipe': 'Pizza', 'unit':'blank'},
                   {'rawFood': 'strong flour', 'amount' : '200', 'recipe': 'Pizza', 'unit':'gram'},
                   {'rawFood': 'vegetable oil', 'amount' : '1', 'recipe': 'Mix', 'unit':'tablespoon'},
                   {'rawFood': 'big potato', 'amount' : '1', 'recipe': 'Baked potato', 'unit':'blank'},
                   {'rawFood': 'cheese', 'amount' : '100', 'recipe': 'Baked potato', 'unit':'gram'},
                   {'rawFood': 'baked beans', 'amount' : '400', 'recipe': 'Baked potato', 'unit':'gram'},
                   {'rawFood': 'onion', 'amount' : '1', 'recipe': 'Roast veg and feta', 'unit':'blank'},
                   {'rawFood': 'courgette', 'amount' : '1', 'recipe': 'Roast veg and feta', 'unit':'blank'},
                   {'rawFood': 'aubergine', 'amount' : '1', 'recipe': 'Roast veg and feta', 'unit':'blank'},
                   {'rawFood': 'pepper', 'amount' : '1', 'recipe': 'Roast veg and feta', 'unit':'blank'},
                   {'rawFood': 'feta', 'amount' : '150', 'recipe': 'Roast veg and feta', 'unit':'gram'},
                   {'rawFood': 'macaroni pasta', 'amount' : '400', 'recipe': 'Macaroni cheese', 'unit':'gram'},
                   {'rawFood': 'butter', 'amount' : '50', 'recipe': 'Macaroni cheese', 'unit':'gram'},
                   {'rawFood': 'plain flour', 'amount' : '50', 'recipe': 'Macaroni cheese', 'unit':'gram'},
                   {'rawFood': 'milk', 'amount' : '150', 'recipe': 'Macaroni cheese', 'unit':'millilitre'},
                   {'rawFood': 'cheese', 'amount' : '200', 'recipe': 'Macaroni cheese', 'unit':'gram'},
                   {'rawFood': 'onion', 'amount' : '1', 'recipe': 'Chilli con carne', 'unit':'blank'},
                   {'rawFood': 'carrot', 'amount' : '1', 'recipe': 'Chilli con carne', 'unit':'blank'},
                   {'rawFood': 'mince', 'amount' : '500', 'recipe': 'Chilli con carne', 'unit':'gram'},
                   {'rawFood': 'black beans', 'amount' : '300', 'recipe': 'Chilli con carne', 'unit':'gram'},
                   {'rawFood': 'tomato sauce', 'amount' : '200', 'recipe': 'Chilli con carne', 'unit':'millilitre'},
                   {'rawFood': 'smoked paprika', 'amount' : '1', 'recipe': 'Chilli con carne', 'unit':'dash'},
                   {'rawFood': 'onion', 'amount' : '1', 'recipe': 'Stir fry', 'unit':'blank'},
                   {'rawFood': 'pepper', 'amount' : '1', 'recipe': 'Stir fry', 'unit':'blank'},
                   {'rawFood': 'bean sprouts', 'amount' : '50', 'recipe': 'Stir fry', 'unit':'gram'},
                   {'rawFood': 'peas', 'amount' : '50', 'recipe': 'Stir fry', 'unit':'gram'},
                   {'rawFood': 'ginger', 'amount' : '1', 'recipe': 'Stir fry', 'unit':'stem'},
                   {'rawFood': 'stir fry sauce', 'amount' : '25', 'recipe': 'Stir fry', 'unit':'millilitre'},
                   {'rawFood': 'noodles', 'amount' : '200', 'recipe': 'Stir fry', 'unit':'gram'}]

    # Recipe list
    recipes = [
               {'name': 'Dutch butter cake', 'categories': ['snack','easy','vegetarian'], 'rating': 4.0,
                'difficulty': 0.5, 'time': 70.0, 'imagePath': 'DutchButterCake/dutchButterCake.png', },
               {'name': 'Burger', 'categories': ['main','dessert','medium'], 'rating': 0.0,
                'difficulty': 2.0, 'time': 30.0, 'imagePath': 'Burger/burger.jpg'},
               {'name': 'Dahl curry', 'categories': ['main','lunch','dinner','easy','vegan','vegetarian'], 'rating': 5.0,
                'difficulty': 5.0, 'time': 30.0, 'imagePath': 'DahlCurry/dahlCurry.png'},
               {'name': 'Pizza', 'categories': ['main','lunch','dinner','medium','vegetarian'], 'rating': 3.5,
                'difficulty': 4.0, 'time': 120.0, 'imagePath': 'Pizza/pizza.jpg'},
                {'name': 'Mix', 'categories': ['main','lunch','easy','vegan','vegetarian'], 'rating': 1.5,
                'difficulty': 0.5, 'time': 40.0, 'imagePath': 'Mix/mix.jpg'},
                {'name': 'Baked potato', 'categories': ['main','dinner','easy','lunch','vegetarian'], 'rating': 4.5,
                'difficulty': 1.0, 'time': 40.0, 'imagePath': 'BakedPotato/bakedPotato.png'},
                {'name': 'Roast veg and feta', 'categories': ['starter','dinner','easy','vegetarian','salad'], 'rating': 1.5,
                'difficulty': 1.0, 'time': 40.0, 'imagePath': 'RoastVegAndFeta/roastVegAndFeta.png'},
                {'name': 'Macaroni cheese', 'categories': ['main','dinner','medium','vegetarian'], 'rating': 5.0,
                'difficulty': 3.0, 'time': 30.0, 'imagePath': 'MacaroniCheese/macaroniCheese.png'},
                {'name': 'Chilli con carne', 'categories': ['main','dinner','medium'], 'rating': 4.0,
                'difficulty': 2.5, 'time': 30.0, 'imagePath': 'ChilliConCarne/chilliConCarne.png'},
                {'name': 'Stir fry', 'categories': ['main','dinner','easy','vegetarian','quick'], 'rating': 3.0,
                'difficulty': 1.5, 'time': 20.0, 'imagePath': 'StirFry/stirFry.png'}]

    # Instruction list
    instructions = [
                    {'step': 1, 'recipe': 'Dutch butter cake', 'media': None, 'description': 'Preheat oven to gas 3 (140 degrees Celsius).'},
                    {'step': 2, 'recipe': 'Dutch butter cake', 'media': None, 'description': 'Grease a shallow cake tin of about 20-22 cm diameter with a little butter. It is very helpful if your tin has slanted edges.'},
                    {'step': 3, 'recipe': 'Dutch butter cake', 'media': None, 'description': 'Mix the flour, sugar, butter and vanilla essence and knead into a supple ball of dough in a large mixing bowl. It may help to cut the butter into small pieces with two knives first, before mixing with your hands. '},
                    {'step': 4, 'recipe': 'Dutch butter cake', 'media': None, 'description': 'Press the dough into the form, making sure there is slightly more dough peripherally, to avoid the edge from overcooking.'},
                    {'step': 5, 'recipe': 'Dutch butter cake', 'media': None, 'description': 'Place on a high shelf and check after about 35 minutes. Only check by eye, it should look slightly underdone, if it is browning then it is probably too far gone as the edge will set rock-hard when it cools. It should look like raw dough in the middle but nowhere should be darker than golden buttery yellow.'},
                    {'step': 6, 'recipe': 'Dutch butter cake', 'media': None, 'description': 'Take the tin from the oven- it is okay if it looks very fluid as this will set when cooling. Cut into diamonds of about 3 x 3 cms, as the pieces are very calorific. Cut the cake when it is lukewarm, that is easier than when it is completely cold.'},
                    {'step': 1, 'recipe': 'Burger', 'media': None, 'description': 'Preheat the oven to what is needed for you beef burgers.'},
                    {'step': 2, 'recipe': 'Burger', 'media': None, 'description': 'When the oven is at the appropriate temperature, put the burger buns in for the time specified for them.'},
                    {'step': 3, 'recipe': 'Burger', 'media': None, 'description': 'Slice your tomato and lettuce leaves to what you want and butter your buns.'},
                    {'step': 4, 'recipe': 'Burger', 'media': None, 'description': 'Build your burger in the manner that you want.'},
                    {'step': 1, 'recipe': 'Dahl curry', 'media': None, 'description': 'Dice the onion and fry in a splash of oil.'},
                    {'step': 2, 'recipe': 'Dahl curry', 'media': None, 'description': 'Add the curry paste and mix.'},
                    {'step': 3, 'recipe': 'Dahl curry', 'media': None, 'description': 'Add lentils and stock, and simmer for 20 minutes until cooked through.'},
                    {'step': 1, 'recipe': 'Pizza', 'media': None, 'description': 'Mix the yeast into the flour.'},
                    {'step': 2, 'recipe': 'Pizza', 'media': None, 'description': 'Add olive oil and 75ml of warm water.'},
                    {'step': 3, 'recipe': 'Pizza', 'media': None, 'description': 'Mix untill it forms a dough.'},
                    {'step': 4, 'recipe': 'Pizza', 'media': None, 'description': 'Leace the dough to rise for 1 hour.'},
                    {'step': 5, 'recipe': 'Pizza', 'media': None, 'description': 'Preheat the oven to 200 degrees Celsius.'},
                    {'step': 6, 'recipe': 'Pizza', 'media': None, 'description': 'Knock the dough back and roll out pizza bases.'},
                    {'step': 7, 'recipe': 'Pizza', 'media': None, 'description': 'Dice onion and spread over pizza base with tomato sauce.'},
                    {'step': 8, 'recipe': 'Pizza', 'media': None, 'description': 'Grate cheese and sprinkle on top and the place in oven for 30 minutes.'},
                    {'step': 1, 'recipe': 'Mix', 'media': None, 'description': 'Preheat oven to 200 degrees Celsius.'},
                    {'step': 2, 'recipe': 'Mix', 'media': None, 'description': 'Take whatever vegetables you wish to use and cut them as you desire.'},
                    {'step': 3, 'recipe': 'Mix', 'media': None, 'description': 'Place all on baking tray with a drizzle of vegetable oil and roast for 35 minutes.'},
                    {'step': 1, 'recipe': 'Baked potato', 'media': None, 'description': 'Preheat oven to 200 degrees Celsius.'},
                    {'step': 2, 'recipe': 'Baked potato', 'media': None, 'description': 'Cut potato open and bake for 30 minutes.'},
                    {'step': 3, 'recipe': 'Baked potato', 'media': None, 'description': 'Heat beans in a pan and then pour over potato.'},
                    {'step': 4, 'recipe': 'Baked potato', 'media': None, 'description': 'Grate cheese and sprinkle on top.'},
                    {'step': 1, 'recipe': 'Roast veg and feta', 'media': None, 'description': 'Preheat oven to 190 degrees Celsius.'},
                    {'step': 2, 'recipe': 'Roast veg and feta', 'media': None, 'description': 'Cut all vegetables into large chunks'},
                    {'step': 3, 'recipe': 'Roast veg and feta', 'media': None, 'description': 'Cube the feta, and toss with the vegetables into a baking tray.'},
                    {'step': 4, 'recipe': 'Roast veg and feta', 'media': None, 'description': 'Place in oven for 35 minutes.'},
                    {'step': 1, 'recipe': 'Macaroni cheese', 'media': None, 'description': 'Preheat oven to 200 degrees Celsius.'},
                    {'step': 2, 'recipe': 'Macaroni cheese', 'media': None, 'description': 'Cook pasta to packet instructions.'},
                    {'step': 3, 'recipe': 'Macaroni cheese', 'media': None, 'description': 'Melt butter in sauce pan and stir in the flour.'},
                    {'step': 4, 'recipe': 'Macaroni cheese', 'media': None, 'description': 'Add milk slowly while stirring continuously until sauce thickens.'},
                    {'step': 5, 'recipe': 'Macaroni cheese', 'media': None, 'description': 'Grate and add the cheese to the sauce.'},
                    {'step': 6, 'recipe': 'Macaroni cheese', 'media': None, 'description': 'Place the pasta in a tray and pour sauce over it.'},
                    {'step': 7, 'recipe': 'Macaroni cheese', 'media': None, 'description': 'Bake for 15 minutes.'},
                    {'step': 1, 'recipe': 'Chilli con carne', 'media': None, 'description': 'Chop and fry onion and carrot.'},
                    {'step': 2, 'recipe': 'Chilli con carne', 'media': None, 'description': 'Add mince and cook till brown.'},
                    {'step': 3, 'recipe': 'Chilli con carne', 'media': None, 'description': 'Add tomato sauce and beans to the mix.'},
                    {'step': 4, 'recipe': 'Chilli con carne', 'media': None, 'description': 'Simmer for 10 minutes.'},
                    {'step': 5, 'recipe': 'Chilli con carne', 'media': None, 'description': 'Flavour with paprika and whatever other spices you want.'},
                    {'step': 1, 'recipe': 'Stir fry', 'media': None, 'description': 'Chop onion, pepper and ginger.'},
                    {'step': 1, 'recipe': 'Stir fry', 'media': None, 'description': 'Fry with peas and sprouts.'},
                    {'step': 1, 'recipe': 'Stir fry', 'media': None, 'description': 'Boil noodles for 3 minutes.'},
                    {'step': 1, 'recipe': 'Stir fry', 'media': None, 'description': 'Add  noodles and sauce to the vegetables.'}]


    # Populate database
    for type in categories:
        c = Category.objects.get_or_create(category=type['category'],
                                           description=type['description'])[0]
        c.save()

    for plan in recipes:
        r = Recipe.objects.get_or_create(name=plan['name'],
                                         rating=plan['rating'],
                                         time=plan['time'],
                                         difficulty=plan['difficulty'],
                                         imagePath=plan['imagePath'])[0]
        r.save()
        for cat in plan['categories']:
            category = Category.objects.get(category=cat)
            r.category.add(category)

    for food in ingredients:
        measurement = Measurement.objects.get(unit=food['unit'])
        raw_food = RawFood.objects.get(name=food['rawFood'])
        plan = Recipe.objects.get(name=food['recipe'])
        i = Ingredient.objects.get_or_create(amount=food['amount'], rawFood=raw_food, recipe=plan, measuredIn=measurement)[0]
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
