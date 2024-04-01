from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from recipes.models import Recipe


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "sandbox/index.html", context)


class RecipeListView(ListView):
    model = Recipe
    template_name = "sandbox/index.html"


    context_object_name = "recipes"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "sandbox/recipe_detail.html"
    context_object_name = "recipe"
