from django import forms
from django.contrib.auth.models import User

class RecipeForm(forms.ModelForm):
    # TODO 
    pass

class ContactForm(forms.Form):
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    phonenumber = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
