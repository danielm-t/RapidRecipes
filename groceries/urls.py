from operator import index
from django.conf.urls import url
from django.urls import path
from groceries import views

app_name = 'groceries'
urlpatterns = [
    path('', views.index, name='index'),
]