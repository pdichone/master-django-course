from django.urls import path

from recipes import views


app_name = "recipes"
urlpatterns = [
    path("", views.recipes, name="index"),
    path(
        "<int:recipe_id>",
        views.recipe, name="recipe_detail"
    ),
]
