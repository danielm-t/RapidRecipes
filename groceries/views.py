from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from groceries.models import UserProfile


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserProfile(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserProfile()
    return render(request,'groceries/register.html',
context = {'user_form': user_form,
'registered': registered})
                
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
    # TODO
    return render(request, 'groceries/shoppinglist')
