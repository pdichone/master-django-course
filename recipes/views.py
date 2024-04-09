from django.shortcuts import get_object_or_404, redirect, render
from comments.forms import CommentForm
from .models import Recipe
from django.contrib.auth.decorators import login_required


def recipes(request):

    recipes = Recipe.objects.all().order_by("-date_added")
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


@login_required
def toggle_favorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.user in recipe.favorited_by.all():
        recipe.favorited_by.remove(request.user)
    else:
        recipe.favorited_by.add(request.user)
    return redirect("recipes:recipe_detail", recipe_id=recipe_id)


@login_required
def favorite_recipes(request):
    user = request.user
    favorites = user.favorite_recipes.all()
    context = {"recipes": favorites}
    return render(request, "recipes/favorite_recipes.html", context)
