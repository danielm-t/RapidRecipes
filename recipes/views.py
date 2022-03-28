from django.shortcuts import render, redirect
from django.http import HttpResponse
from recipes.models import Category, Recipe, Ingredient, Instruction
from food.models import RawFood, Measurement
from recipes.forms import ContactForm, FilterForm
from django.core.mail import send_mail, BadHeaderError
from rapid_recipes.settings import DEFAULT_FROM_EMAIL
from django.core.files.storage import default_storage


# Create your views here.

def index(request):
    a = 0
    if request.method == 'GET':
        form = FilterForm()
        context_dict = {}
        recipe_list = Recipe.objects.order_by('-rating')
        context_dict = {'recipes': recipe_list, 'form':form}
    elif request.method == 'POST':
        context_dict = {}
        form = FilterForm(request.POST)

        categories = []
        for key, value in form.data.items():
            if key == 'csrfmiddlewaretoken':
                continue
            else:
                categories.append(key)

        if categories:
            recipe_list = Recipe.objects

            for category in categories:
                c = Category.objects.get(category=category)
                recipe_list = recipe_list.filter(category=c)
            
            recipe_list = recipe_list.order_by('-rating')
        else:
            recipe_list = Recipe.objects.order_by('-rating')
        
        context_dict = {'recipes': recipe_list, 'form':form}
    return render(request, "recipes/index.html", context_dict)

def about(request):
    response = render(request, 'recipes/about.html')
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
    
def show_recipe(request, recipe_name_slug):
    context_dict = {}
    try:
        recipe = Recipe.objects.get(slug=recipe_name_slug)
        recommended_recipes = Recipe.objects.order_by('-rating').exclude(id=recipe.id)[:5]
        ingredients = recipe.ingredient_set.all()
        instructions = recipe.instruction_set.all()
        
        context_dict['recipe'] = recipe
        context_dict['ingredients'] = ingredients
        context_dict['instructions'] = instructions
        context_dict['recommended_recipes'] = recommended_recipes
        
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
                instructionimagepaths.append(f"recipes/{instructionimagepath}")
            else:
                instructionimagepaths.append(None)

        # categories
        recipe = Recipe.objects.get_or_create(name=name,
                        rating=rating,
                        difficulty=difficulty,
                        time=time,
                        imagePath = recipeimagepath)[0]
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
    

def search(request):
    if request.method == "POST":
        search = request.POST['search']
        recipes = Recipe.objects.filter(name__icontains=search)
        a = 0
        context_dict = {'search':search, 'recipes':recipes}
        response = render(request, 'recipes/search.html', context_dict)
        return response
    if request.method == 'GET':
        return redirect('index')
