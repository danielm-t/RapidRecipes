from pickletools import read_uint1
from django import forms
from django.db import models
from django.contrib.auth.models import User
from recipes.models import Instruction, Recipe, Ingredient, Category

class ContactForm(forms.Form):
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    phonenumber = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class FilterForm(forms.Form):
    lunch = forms.BooleanField(label='lunch', required=False)
    dinner = forms.BooleanField(label='dinner', required=False)
    breakfast = forms.BooleanField(label='breakfast', required=False)
    easy = forms.BooleanField(label='easy', required=False)
    medium = forms.BooleanField(label='medium', required=False)
    hard = forms.BooleanField(label='hard', required=False)
    drink = forms.BooleanField(label='drink', required=False)
    vegan = forms.BooleanField(label='vegan', required=False)
    vegetarian = forms.BooleanField(label='vegetarian', required=False)
    beef = forms.BooleanField(label='beef', required=False)
    chicken = forms.BooleanField(label='chicken', required=False)
    fish = forms.BooleanField(label='fish', required=False)
    
    