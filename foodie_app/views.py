from django.shortcuts import get_object_or_404, redirect, render

from foodie_app.forms import CategoryForm, RecipeForm
from .models import Category
from recipes.models import Recipe
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {"categories": categories}

    return render(request, "foodie_app/index.html", context)


def recipes(request, category_id):
    recipes = Recipe.objects.filter(category=category_id)
    category = Category.objects.get(pk=category_id)

    context = {"recipes": recipes, "category": category}
    return render(request, "foodie_app/recipes.html", context)


@login_required
def add_category(request):
    if request.method == "POST":

        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("foodie_app:index")
        else:
            return render(request, "foodie_app/add_category.html", context)
    else:
        form = CategoryForm()
        context = {"form": form}

        return render(request, "foodie_app/add_category.html", context)


@login_required
def add_recipe(request, category_id=None):
    category = None
    if category_id:
        # category = Category.objects.get(pk=category_id)
        category = get_object_or_404(Category, id=category_id)
        form = RecipeForm(request.POST or None, initial={"category": category})
    else:
        form = RecipeForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.user = request.user
        new_recipe.save()
        return redirect("foodie_app:recipes", category_id=new_recipe.category.id)

    context = {"form": form, "category": category}
    return render(request, "foodie_app/add_recipe.html", context)
