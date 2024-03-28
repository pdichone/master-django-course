from django.urls import path
from . import views

app_name = "foodie_app"
urlpatterns = [path("", views.index)]
