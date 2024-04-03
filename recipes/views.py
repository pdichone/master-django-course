from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from foodie_app.forms import RecipeForm
from foodie_app.models import Category
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


def add_recipe(request, category_id=None):
    category = None
    if category_id:
        # category = Category.objects.get(pk=category_id)
        category = get_object_or_404(Category, id=category_id)
        form = RecipeForm(request.POST or None, initial={"category": category})
    else:
        form = RecipeForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_recipe = form.save()
        return redirect("foodie_app:recipes", category_id=new_recipe.category.id)

    context = {"form": form, "category": category}
    return render(request, "recipes/add_recipe.html", context)
