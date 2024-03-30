from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def comments(request):
    return HttpResponse("Hello from Comments")
