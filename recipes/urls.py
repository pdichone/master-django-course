from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipes import views


app_name = "recipes"

router = DefaultRouter()
router.register(r"recipes", views.RecipeViewSet, basename="recipe")

urlpatterns = [
    path("", views.recipes, name="index"),
    path("<int:recipe_id>", views.recipe_detail, name="recipe_detail"),
    path(
        "<int:recipe_id>/toggle_favorite", views.toggle_favorite, name="toggle_favorite"
    ),
    path("my-favorites/", views.favorite_recipes, name="favorite_recipes"),
    path("search/", views.search_results, name="search_results"),
    path("<int:recipe_id>/delete/", views.delete_recipe, name="delete_recipe"),
    path("<int:recipe_id>/edit/", views.edit_recipe, name="edit_recipe"),
    path("api/", include(router.urls)),
]
