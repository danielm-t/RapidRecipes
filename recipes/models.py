from django.db import models
from django.template.defaultfilters import slugify
from food.models import RawFood

class Category(models.Model):
    CATEGORY_MAX_LENGTH = 255
    TEXT_MAX_LENGTH = 255
    
    category = models.CharField(max_length=CATEGORY_MAX_LENGTH, unique=True)
    description = models.CharField(max_length=TEXT_MAX_LENGTH, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Recipe(models.Model):

    NAME_MAX_LENGTH = 255
    IMAGE_PATH_MAX_LENGTH = 255
    RATING_MAX_SIZE = 5
    DIFFICULTY_MAX_SIZE = 5

    name = models.CharField(max_length=NAME_MAX_LENGTH)
    category = models.ManyToManyField(Category, blank=True)
    rating = models.FloatField(max_length=RATING_MAX_SIZE, default=0)
    imagePath = models.CharField(max_length=IMAGE_PATH_MAX_LENGTH, blank=True)
    difficulty = models.FloatField(max_length=DIFFICULTY_MAX_SIZE)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Ingredient(models.Model):

    AMOUNT_MAX_LENGTH = 50

    rawFood = models.ForeignKey(RawFood, on_delete=models.CASCADE) # If a raw food is deleted, delete ingredient
    amount = models.CharField(max_length=AMOUNT_MAX_LENGTH)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) # Ingredient belongs to a recipe
    def __str__(self):
        return self.rawFood.name


class Instruction(models.Model):
    MEDIA_PATH_MAX_LENGTH = 255

    step = models.SmallIntegerField()
    description = models.TextField()
    media = models.CharField(max_length=MEDIA_PATH_MAX_LENGTH, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE) # Instruction belongs to a recipe
    def __str__(self):
        return self.step


