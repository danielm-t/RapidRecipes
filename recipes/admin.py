from django.contrib import admin
from recipes.models import Category, Recipe, Ingredient, Instruction
from groceries.models import GroceryItem, UserProfile
from food.models import Measurement, RawFood


admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(GroceryItem)
admin.site.register(UserProfile)
admin.site.register(Measurement)
admin.site.register(RawFood)


# Register your models here.
