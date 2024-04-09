from django.urls import path

from recipes import views


app_name = "recipes"
urlpatterns = [
    path("", views.recipes, name="index"),
    path("<int:recipe_id>", views.recipe_detail, name="recipe_detail"),
    path(
        "<int:recipe_id>/toggle_favorite", views.toggle_favorite, name="toggle_favorite"
    ),
    path("my-favorites/", views.favorite_recipes, name="favorite_recipes"),
]
