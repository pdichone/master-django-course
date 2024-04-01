from django.shortcuts import render
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