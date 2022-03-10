from operator import index
from django.conf.urls import url
from django.urls import path
from recipes import views

app_name = 'recipes'
urlpatterns = [
    path('', views.index, name='index'),
]
