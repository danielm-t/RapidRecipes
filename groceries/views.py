from django.shortcuts import render
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
                
# Create your views here.
