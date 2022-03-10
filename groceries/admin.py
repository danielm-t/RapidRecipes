from django.contrib import admin

from groceries.models import GroceryItem, UserProfile

admin.site.register(UserProfile)
# Register your models here.
admin.site.register(GroceryItem)
admin.site.register(UserProfile)
