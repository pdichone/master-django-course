from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from comments.forms import CommentForm
from foodie_app.forms import RecipeForm
from foodie_app.models import Category
from .models import Recipe
from django.db.models import Q


def recipes(request):

    recipes = Recipe.objects.all()
    context = {"recipes": recipes}

    return render(request, "recipes/recipes.html", context)


def recipe_detail(request, recipe_id):

    # recipe = Recipe.objects.get(id=recipe_id)
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comments = recipe.comments.all()

    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.user = request.user
            new_comment.save()
            return redirect(
                recipe.get_absolute_url()
            )  # Redirect to the same recipe page - refresh
    else:
        comment_form = CommentForm()

    context = {"recipe": recipe, "comments": comments, "comment_form": comment_form}
    return render(request, "recipes/recipe.html", context)
