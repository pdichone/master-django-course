from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe
from django.db.models import Q


# Create your views here.
def recipes(request):
    # recipes = Recipe.objects.filter(category__name__exact="Soup")
    # recipes = Recipe.objects.exclude(name__contains="chocolate")
    # recipes = (
    #     Recipe.objects.filter(category__name__exact="Soup")
    #     .exclude(name__contains="chocolate")
    #     .order_by("-date_added")
    # )
    # recipes = Recipe.objects.all()[:2]
    # recipes = Recipe.objects.aggregate(Count("id"))
    # recipes = Recipe.objects.aggregate(Avg("id"))
    # recipes = Recipe.objects.filter(id__gt=3)
    # recipes = Recipe.objects.filter(
    #     Q(name__startswith="M") | Q(description__icontains="Cuban")
    # )
    recipes = Recipe.objects.filter(name__contains="Bread").exists()

    print("Recipes", recipes)

    return HttpResponse("Hello from Recipes")
