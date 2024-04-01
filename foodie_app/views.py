from django.shortcuts import redirect, render

from foodie_app.forms import CategoryForm
from .models import Category
from recipes.models import Recipe


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
