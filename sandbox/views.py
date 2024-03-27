from django.http import HttpResponse
from django.shortcuts import render
from random import choice

fruits = ["apples", "pears", "mangoes"]


# Create your views here.
def index(request):

    data = choice(fruits)
    return HttpResponse(f"Hello there {data}")
