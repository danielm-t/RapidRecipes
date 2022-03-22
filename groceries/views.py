from calendar import c
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from groceries.models import UserProfile, GroceryItem
from recipes.models import Measurement
from food.models import RawFood
from django.contrib.auth.models import User
from groceries.forms import UserForm


def register(request):
    registered = False
    context = {'registered': registered}
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            login(request, user)
            return redirect(reverse('index'))
        else:
            print(user_form.errors)
            context['form'] = user_form
    return render(request,'groceries/register.html', context)
                
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return HttpResponse("Your account is currently disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'groceries/login.html')

@login_required
def user_logout(request):

    logout(request)

    return redirect(reverse('index'))

@login_required
def shopping_list(request):
    context = {'rawFoods' : RawFood.objects.all()}
    context['groceries'] = GroceryItem.objects.filter(user=request.user)
    return render(request, 'groceries/shoppinglist.html', context)


def get_added_grocery(request):
    if request.method == "GET":
        get = request.GET
        user = request.user
        ingredient = get.get("i", None)
        measurement = get.get("m", None)
        amount = get.get("a", None)
        owned = get.get("o", None)
        if owned:
            owned = not (owned == "false")
        else:
            owned = False
        context={}
        try:
            rawFood = RawFood.objects.get(name=ingredient)
            measuredIn = Measurement.objects.get(unit=measurement)
            grocery = GroceryItem.objects.create(rawFood=rawFood,
                                                        amount=amount,
                                                        available=owned,
                                                        user=user,
                                                        measuredIn=measuredIn)[0]
            grocery.save()
            context['groceries'] = GroceryItem.objects.filter(user=request.user)
        except (RawFood.DoesNotExist, Measurement.DoesNotExist) as e:
            context['groceries'] = GroceryItem.objects.filter(user=request.user)
        return render(request, "groceries/table_body.html", context)

def delete_grocery(request):
    if request.method == "GET":
        get = request.GET
        user = request.user
        ingredient = get.get("i", None)
        measurement = get.get("m", None)
        amount = get.get("a", None)
        owned = get.get("o", None)
        if owned:
            owned = not (owned == "false")
        else:
            owned = False
        context = {}
        try:
            rawFood = RawFood.objects.get(name=ingredient)
            measuredIn = Measurement.objects.get(unit=measurement)
            GroceryItem.objects.filter(rawFood=rawFood, amount=amount, available=owned, user=user, measuredIn=measuredIn).delete()
            context['groceries'] = GroceryItem.objects.filter(user=request.user)
            print("hey")
        except (RawFood.DoesNotExist, Measurement.DoesNotExist) as e:
            context['groceries'] = GroceryItem.objects.filter(user=request.user)
        return render(request, "groceries/table_body.html", context)

