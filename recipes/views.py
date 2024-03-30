from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe


# Create your views here.
def recipes(request):
    # recipes = Recipe.objects.filter(category__name__exact="Soup")
    # recipes = Recipe.objects.exclude(name__contains="chocolate")
    recipes = (
        Recipe.objects.filter(category__name__exact="Soup")
        .exclude(name__contains="chocolate")
        .order_by("-date_added")
    )

    print("Recipes", recipes)

    return HttpResponse("Hello from Recipes")
