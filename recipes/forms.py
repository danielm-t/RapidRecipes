from pickletools import read_uint1
from django import forms
from django.db import models
from django.contrib.auth.models import User
from recipes.models import Instruction, Recipe, Ingredient, Category



class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('slug', )
    try:
            widgets = {
            'category' : forms.CheckboxSelectMultiple(
                choices=Category.objects.all()),
                    'rating' : forms.NumberInput(attrs={'step': 0.1, 'min': 0.0, 'max': 5.0, "class": "col"}),
                    'imagePath' : forms.FileInput(),
                    'difficulty' : forms.NumberInput(attrs={'step': 0.1, 'min': 0.0, 'max': 5.0})
            }
    except:
        pass

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = ('recipe',)

IngredientFormSet = forms.inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=1, max_num=50, can_delete=True)

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        exclude = ('recipe', )

InstructionFormSet = forms.inlineformset_factory(Recipe, Instruction, form=InstructionForm)

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

    
    