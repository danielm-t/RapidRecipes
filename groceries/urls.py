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
    path('shoppinglist/', views.shoppinglist, name='shoppinglist'),
]