from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    data = {"name": "Paulo", "age": 123}

    context = {"data": data}
    return render(request, "sandbox/index.html", context)
