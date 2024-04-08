from django.urls import path
from . import views

app_name = "sandbox"
# https://mysite.com/
urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipes/<int:pk>", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path("refreshing/", views.SpecifcRecipesView.as_view(), name="refreshing_recipes"),
    path("feedback/", views.feedback, name="feedback"),
    path("feedback/review", views.feedback_review, name="feedback_review"),
    path("thank-you/", views.thank_you, name="thank_you"),
]
