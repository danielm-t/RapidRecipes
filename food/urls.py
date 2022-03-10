from operator import index
from django.conf.urls import url
from django.urls import path
from food import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
]