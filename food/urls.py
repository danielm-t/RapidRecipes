from operator import index
from django.conf.urls import url
from django.urls import path
from food import views
from recipes.views import index as recipe_index

app_name = 'food'
urlpatterns = [
    path('', recipe_index, name='index'),
    path('ajax/get/getRawFoodMeasurementTypes', views.getRawFoodMeasurementTypes, name="getRawFoodMeasurementTypes")
]