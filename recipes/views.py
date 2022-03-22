from email.mime import image
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from recipes.models import Category, Recipe, Ingredient, Instruction
from food.models import RawFood, Measurement
from recipes.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from rapid_recipes.settings import DEFAULT_FROM_EMAIL
from django.core.files.storage import default_storage


# Create your views here.

def index(request):
    context_dict = {}
    recipe_list = Recipe.objects.order_by('-rating')[:5]
    context_dict = {'recipes': recipe_list}
    #visitor_cookie_handler(request)
    response = render(request, 'recipes/index.html', context_dict)
    return response

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
            return redirect('index')
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
        categories = Category.objects.all()
        rawFoods = RawFood.objects.all()

        context_dict = {
            "categories" : categories,
            "rawFoods" : rawFoods,
            }
        return render(request, 'recipes/add_recipe.html', context_dict)
    else:
    
        # Handle Post
        post = request.POST
        name = post['recipename']
        time = post['time']
        rating = post['rating']
        difficulty = post['difficulty']

        # Get categories as list
        categories = post.getlist("categories")

        # Get ingredients, their amounts and measurements as a list
        ingredients = post.getlist("ingredient")
        ingredientamounts = post.getlist("ingredientamount")
        ingredientmeasurements = post.getlist("ingredientmeasurement")

        # Get instructions as a list
        instructions = post.getlist("instruction")
        
        files = request.FILES

        instructionimages = []
        for i in range(len(instructions)):
            try:
                imagename = f"instructionimage{i+1}"
                image = files[imagename]
                instructionimages.append(image)
            except:
                instructionimages.append(None)
        

        recipeimage = files['recipeimage']
        suffix = recipeimage.name.rsplit(".", 1)[-1]

        recipeimagepath = f"{name}/{name}.{suffix}"
        default_storage.save(f"recipes/{recipeimagepath}", recipeimage)


        instructionimagepaths = []
        for (i, ii) in enumerate(instructionimages):
            if ii != None:
                suffix = ii.name.rsplit(".", 1)[-1]

                instructionimagepath = f"{name}/instructions/instruction{i}.{suffix}"
                default_storage.save(f"recipes/{instructionimagepath}", ii)
                instructionimagepaths.append(instructionimagepath)
            else:
                instructionimagepaths.append(None)
                


        categories
        recipe = Recipe.objects.get_or_create(name=name,
                        rating=rating,
                        difficulty=difficulty,
                        time=time,
                        imagePath=recipeimagepath)[0]
        recipe.save()

        for category in categories:
            c = Category.objects.get(category=category)
            recipe.category.add(c)
        
        
        
        for (i, ia, im) in zip(ingredients, ingredientamounts, ingredientmeasurements):
            m = Measurement.objects.get(unit=im)
            f = RawFood.objects.get(name=i)
            ingredient = Ingredient.objects.get_or_create(amount=ia,
                                                            rawFood=f, 
                                                            recipe=recipe,
                                                            measuredIn=m)[0]
            ingredient.save()


        for i in range(len(instructions)):
            if instructionimages[i] != None:
                instruction = Instruction.objects.get_or_create(step=i+1,
                                                                description=instructions[i],
                                                                media=instructionimagepaths[i],
                                                                recipe=recipe)[0]
            else:
                instruction = Instruction.objects.get_or_create(step=i+1,
                                                                description=instructions[i],
                                                                recipe=recipe)[0]
            instruction.save()

        return redirect('index')
    


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