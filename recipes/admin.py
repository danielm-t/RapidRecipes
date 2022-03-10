from django.contrib import admin
from recipes.models import Category, Recipe, Ingredient, Instruction

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)


# Register your models here.
