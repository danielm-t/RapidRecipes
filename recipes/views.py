from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from recipes.models import Category, Recipe, Ingredient, Instruction
from recipes.forms import RecipeForm

# Create your views here.

def index(request):
    context_dict = {}
    recipe_list = Recipe.objects.order_by('-views')[:5]
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'recipes': recipe_list}
    context_dict['categories'] = category_list
    #visitor_cookie_handler(request)
    response = render(request, 'recipes/index.html', context_dict)
    return response

def about(request):
    context_dict = {}
    #print(request.method)
    #print(request.user)

    context_dict['visits'] = request.session['visits']

    response = render(request, 'recipes/about.html', context_dict)
    return response

def contact(request):
    return render(request, 'recipes/contact.html')  

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
        context_dict['ingredient'] = ingredients
        context_dict['instruction'] = instructions
        
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None

    return render(request, 'recipes/recipe.html', context_dict)

@login_required
def add_recipe(request):
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=True)
            print(recipe, recipe.slug)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'recipes/add_recipe.html', {'form': form})


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