from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from recipes.models import Category, Recipe, Ingredient, Instruction
from food.models import RawFood
from .forms import InstructionFormSet, RecipeForm, IngredientFormSet, ContactForm, FilterForm
from django.core.mail import send_mail, BadHeaderError
from rapid_recipes.settings import DEFAULT_FROM_EMAIL

# Create your views here.

def index(request):
    a = 0
    if request.method == 'GET':
        form = FilterForm()
        context_dict = {}
        recipe_list = Recipe.objects.order_by('-rating')[:5]
        context_dict = {'recipes': recipe_list, 'form':form}
        #visitor_cookie_handler(request)
        
    elif request.method == 'POST':
        context_dict = {}
        form = FilterForm(request.POST)
        if 'lunch' in request.POST:
            recipe_list = Recipe.objects.filter(category=6).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        if 'dinner' in request.POST:
            recipe_list = Recipe.objects.filter(category=7).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        if 'breakfast' in request.POST:
            recipe_list = Recipe.objects.filter(category=5).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        if 'easy' in request.POST:
            recipe_list = Recipe.objects.filter(category=14).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        if 'medium' in request.POST:
            recipe_list = Recipe.objects.filter(category=15).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        if 'hard' in request.POST:
            recipe_list = Recipe.objects.filter(category=16).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
       
        if 'drink' in request.POST:
            recipe_list = Recipe.objects.filter(category=8).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        if 'vegan' in request.POST:
            recipe_list = Recipe.objects.filter(category=9).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        if 'vegetarian' in request.POST:
            recipe_list = Recipe.objects.filter(category=10).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        if 'beef' in request.POST:
            recipe_list = Recipe.objects.filter(category=11).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        if 'chicken' in request.POST:
            recipe_list = Recipe.objects.filter(category=12).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        if 'fish' in request.POST:
            recipe_list = Recipe.objects.filter(category=13).order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            a = 1
        
        
        
        elif a == 0:
            form = FilterForm()
            recipe_list = Recipe.objects.order_by('-rating')[:5]
            context_dict = {'recipes': recipe_list, 'form':form}
            return render(request, "recipes/index.html", context_dict)
            
    return render(request, "recipes/index.html", context_dict)

def about(request):
    context_dict = {}
    #print(request.method)
    #print(request.user)

    #context_dict['visits'] = request.session['visits']

    response = render(request, 'recipes/about.html', context_dict)
    return response

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']
            message = form.cleaned_data['message']

            message_with_user_info = "Name: " + lastname + ", " + firstname + "\n" + "Email: " + email + "\n"
            if phonenumber:
                message_with_user_info += "Phonenumber: " + phonenumber + "\n"
            
            message_with_user_info += message

            try:
                send_mail("Inquiry from User", message_with_user_info, DEFAULT_FROM_EMAIL, [DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "recipes/contact.html", {'form': form})

def success(request):
    return HttpResponse("The email was successfully sent!")


# def show_category(request, category_name_slug):
#     context_dict = {}
#     try:
#         category = Category.objects.get(slug=category_name_slug)
#         recipe = Recipe.objects.filter(category=category)
#         context_dict['recipe'] = recipe
#         context_dict['category'] = category
#     except Category.DoesNotExist:
#         context_dict['category'] = None
#         context_dict['recipe'] = None
#     return render(request, '/category.html', context=context_dict)
    
    
def show_recipe(request, recipe_name_slug):
    context_dict = {}
    try:
        recipe = Recipe.objects.get(slug=recipe_name_slug)
        ingredients = recipe.ingredient_set.all()
        instructions = recipe.instruction_set.all()
        
        context_dict['recipe'] = recipe
        context_dict['ingredients'] = ingredients
        context_dict['instructions'] = instructions
        
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None

    return render(request, 'recipes/view_recipe.html', context_dict)

def add_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        ingredientformset = IngredientFormSet()
        instructionformset = InstructionFormSet()
        categories = Category.objects.all()
        rawFoods = RawFood.objects

        context_dict = {
            "form" : form, 
            "ingredientformset": ingredientformset,
            "instructionformset": instructionformset,
            "categories" : categories,
            "rawFoods" : rawFoods
            }
        return render(request, 'recipes/add_recipe.html', context_dict)
    else:
        post = request.POST
        print(post.getlist("ingredient"))
        print(post.getlist("categories"))
        print(post.getlist("instruction"))

        return HttpResponse("Hello")
    

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        recipesS = Recipe.objects.filter(feeder__icontains=searched)
        
        context_dict = {'searched':searched, 'recipesS':recipesS}
        response = render(request, 'recipes/search.html', context_dict)
        return response
    else:
        context_dict = {}
        response = render(request, 'recipes/search.html', context_dict)
        return response


# def some_view(request):
#     if not request.user.is_authenticated():
#         return HttpResponse("You are logged in.")
#     else:
#         return HttpResponse("You are not logged in.")


# def get_server_side_cookie(request, cookie, default_val=None):
#     val = request.session.get(cookie)
#     if not val:
#         val = default_val
#     return val
    

# def visitor_cookie_handler(request):
#     visits = int(get_server_side_cookie(request, 'visits', '1'))
#     last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
#     last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    
#     if (datetime.now() - last_visit_time).days > 0:
#         visits = visits + 1
#         request.session['last_visit'] = str(datetime.now())
#     else:
#         request.session['last_visit'] = last_visit_cookie
        
#     request.session['visits'] = visits