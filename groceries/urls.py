from operator import index
from django.conf.urls import url
from django.urls import path
from groceries import views
from recipes.views import index as recipe_index

app_name = 'groceries'
urlpatterns = [
    path('', recipe_index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('shoppinglist/', views.shopping_list, name='shoppinglist'),
    path('get_added_grocery/', views.get_added_grocery, name="get_added_grocery"),
    path('delete_grocery/', views.delete_grocery, name="delete_grocery"),
]