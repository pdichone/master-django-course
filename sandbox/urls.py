from django.urls import path
from . import views

# https://mysite.com/
urlpatterns = [path("", views.index)]
