from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe
from django.db.models import Q


def recipes(request):

    recipes = Recipe.objects.all()
    context = {"recipes": recipes}

    return render(request, "recipes/recipes.html", context)


def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {"recipe": recipe}
    return render(request, "recipes/recipe.html", context)
