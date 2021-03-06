from django.urls import path
from recipes import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('<slug:recipe_name_slug>/', views.show_recipe, name='show_recipe'),
    path('search', views.search, name='search'),
]
