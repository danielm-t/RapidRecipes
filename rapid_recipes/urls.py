"""rapid_recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from recipes import views
#from groceries import views
#from food import views
from django.conf import settings
from django.conf.urls.static import static
#app_name='rapid'
urlpatterns = [
#     path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('recipes/', include('recipes.urls')),
#     path('about/', views.about, name='about'),
#     path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
#     path('add_category/', views.add_category, name='add_category'),
#     path('recipes/<slug:recipe_name_slug>/', views.show_recipes, name='show_recipes'),
#     path('add_recipe/', views.add_recipe, name='add_recipe'),
# #    path('register/', views.register, name='register'), 
#     path('login/', views.user_login, name='login'),
#     path('restricted/', views.restricted, name='restricted'),
#     path('logout/', views.user_logout, name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

