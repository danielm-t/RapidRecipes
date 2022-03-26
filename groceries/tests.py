import importlib
from django.test import TestCase
from groceries.models import GroceryItem
from food.tests import CreateRawFood, CreateMeasurement
from django.contrib.auth.models import User
from django.urls import reverse
from groceries.forms import UserForm
from django import forms

# Create your tests here.

def CreateGroceryItem():
    grocery_item = GroceryItem.objects.get_or_create(rawfood=CreateRawFood(),amount=3,available=True,user=CreateUser())
    grocery_item.measuredIn.add(CreateMeasurement())

    return grocery_item

def CreateUser():
    user = User.objects.get_or_create(username='JohnS', first_name='John', last_name='Smith', email='johnsmith@test.com')

    return user


class TestViews(TestCase):

    def setUp(self):
        self.views_module = importlib.import_module('groceries.views')
        self.views_module_listing = dir(self.views_module)

        self.project_urls_module = importlib.import_module('groceries.urls')

    def test_views_are_present(self):

        # Check if register page is present
        register_present = 'register' in self.views_module_listing
        self.assertTrue(register_present, 'FAIL: register not present')

        # Check if login page is present
        login_present = 'login' in self.views_module_listing
        self.assertTrue(login_present, 'FAIL: login not present')

        # Check if logout page is present
        logout_present = 'logout' in self.views_module_listing
        self.assertTrue(logout_present, 'FAIL: logout not present')

        # # Check if shoppinglist page is present
        shoppinglist_present = 'shopping_list' in self.views_module_listing
        self.assertTrue(shoppinglist_present, 'FAIL: shoppinglist not present')

        # Check if get_added_grocery page is present
        get_added_grocery_present = 'register' in self.views_module_listing
        self.assertTrue(get_added_grocery_present, 'FAIL: get_added_grocery not present')

        # Check if delete_grocery page is present
        delete_grocery_present = 'delete_grocery' in self.views_module_listing
        self.assertTrue(delete_grocery_present, 'FAIL: delete_grocery not present')

        # Check if change_amount page is present
        change_amount_present = 'change_amount' in self.views_module_listing
        self.assertTrue(change_amount_present, 'FAIL: change_amount not present')

class TestRegisterForms(TestCase):

    def test_normal_register(self):

        user = {'username': 'johns', 'first_name': 'John', 'last_name': 'Smith', 'email': 'johnsmith@test.com', 'password': 'testing123', 'confirm_password': 'testing123'}

        userform = UserForm(data=user)
        self.assertTrue(userform.is_valid(), 'FAIL: form seen as invalid')
        userObject = userform.save()
        userObject.set_password(user['password'])
        userObject.save()

        self.assertEquals(len(User.objects.all()), 1, 'FAIL: user not created')

        if userObject is not None:
            userObject.delete()

    def test_empty_form(self):
        user = {'username': '', 'first_name': '', 'last_name': '', 'email': '',
                'password': '', 'confirm_password': ''}

        userform = UserForm(data=user)
        self.assertFalse(userform.is_valid(),'FAIL: empty form seen as valid')

    def test_invalid_password(self):
        user = {'username': 'johns', 'first_name': 'John', 'last_name': 'Smith', 'email': 'johnsmith@test.com',
                'password': 'test', 'confirm_password': 'test'}

        data = {**user}
        sending = self.client.post(reverse('groceries:register'), data=data)
        receiving = sending.content.decode('utf-8')
        self.assertRaises(forms.ValidationError)

    def test_already_registered(self):
        user = {'username': 'johns', 'first_name': 'John', 'last_name': 'Smith', 'email': 'johnsmith@test.com',
                'password': 'testing', 'confirm_password': 'testing'}

        data = {**user}
        sending = self.client.post(reverse('groceries:register'), data=data)

        user = {'username': 'johns', 'first_name': 'John', 'last_name': 'Smith', 'email': 'johnsmith@test.com',
                'password': 'testing', 'confirm_password': 'testing'}

        data = {**user}
        sending = self.client.post(reverse('groceries:register'), data=data)
        receiving = sending.content.decode('utf-8')
        self.assertRaises(forms.ValidationError)

    def test_invalid_email(self):
        user = {'username': 'johns', 'first_name': 'John', 'last_name': 'Smith', 'email': 'johnsmith',
                'password': 'testing', 'confirm_password': 'testing'}

        data = {**user}
        sending = self.client.post(reverse('groceries:register'), data=data)
        receiving = sending.content.decode('utf-8')
        self.assertRaises(forms.ValidationError)


class TestLoginForms(TestCase):

    def test_normal_login(self):

        user = {'username': 'johns', 'password': 'testing'}

        userform = UserForm(data=user)
        self.assertTrue(userform.is_valid(), 'FAIL: form seen as invalid')
        userObject = userform.save()
        userObject.set_password(user['password'])
        userObject.save()


        data = {**user}
        sending = self.client.post(reverse('groceries:login'), data=data)
        self.assertEquals(sending.status_code, 302, 'FAIL: user was not logged in')

    def test_invalid_login(self):

        user = {'username': 'invalid', 'password': 'invalid123'}

        data = {**user}
        sending = self.client.post(reverse('groceries:login'), data=data)
        self.assertEquals(sending.status_code, 200, 'FAIL: invalid login was accepted')
