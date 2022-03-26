import importlib
from django.test import TestCase
from recipes.models import Category, Recipe, Ingredient, Instruction
from food.tests import CreateMeasurement, CreateRawFood
from django.urls import reverse

# Create your tests here.

def CreateCategory():
    category = Category.objects.get_or_create(category='Broths', description='These broths good')

    return category


def CreateRecipe():
    recipe = Recipe.objects.get_or_create(name='Chicken Broth',rating=4.5,difficulty=2,time=45)
    recipe.category.add(CreateCategory())

    return recipe


def CreateIngredient():
    ingredient = Ingredient.objects.get_or_create(rawFood=CreateRawFood(), amount=2, recipe=CreateRecipe())

    ingredient.measuredIn.add(CreateMeasurement())

    return ingredient


def CreateInstruction():
    instruction = Instruction.objects.get_or_create(step=1,description='Add Water', recipe=CreateRecipe())

    return instruction


class TestViews(TestCase):

    def setUp(self):
        self.views_module = importlib.import_module('recipes.views')
        self.views_module_listing = dir(self.views_module)

        self.project_urls_module = importlib.import_module('recipes.urls')

    def test_views_are_present(self):

        # Check if index page is present
        index_present = 'index' in self.views_module_listing
        self.assertTrue(index_present, 'FAIL: index not present')

        # Check if add_recipe page is present
        add_recipe_present = 'add_recipe' in self.views_module_listing
        self.assertTrue(add_recipe_present, 'FAIL: add_recipe not present')

        # Check if show_recipe page is present
        show_recipe_present = 'show_recipe' in self.views_module_listing
        self.assertTrue(show_recipe_present, 'FAIL: show_recipe not present')
