from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View

from recipes.models import Recipe, Category
from sandbox.forms import FeedbackForm
from sandbox.models import Feedback
from django.contrib import messages


# Create your views here.
def index(request):

    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "sandbox/index.html", context)


class RecipeListView(ListView):
    model = Recipe
    template_name = "sandbox/index.html"

    context_object_name = "recipes"

    def get_queryset(self):
        filtered_recipes = Recipe.objects.filter(category__name__iexact="soup")
        return filtered_recipes


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "sandbox/recipe_detail.html"
    context_object_name = "recipe"


def thank_you(request):
    return HttpResponse("Thank you for your feedback.")


def feedback(request):
    request.session["feedback_visits"] = request.session.get("feedback_visits", 0) + 1

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():

            # save form data to session
            request.session["feedback_data"] = form.cleaned_data
            return redirect("sandbox:feedback_review")

            # name = form.cleaned_data["name"]
            # email = form.cleaned_data["email"]
            # feedback = form.cleaned_data["feedback"]
            # satisfaction = form.cleaned_data["satisfaction"]
            # Feedback.objects.create(
            #     name=name, email=email, feedback=feedback, satisfaction=satisfaction
            # )
            # messages.add_message(
            #     request, messages.SUCCESS, "Feedback sent successfully!"
            # )
            # messages.success(request, "Feedback sent successfully!")

            # return redirect("sandbox:index")

    else:
        form = FeedbackForm()

    context = {"form": form, "visits": request.session["feedback_visits"]}
    return render(request, "sandbox/feedback_form.html", context)


def feedback_review(request):
    feedback_data = request.session.get("feedback_data", {})
    if request.method == "POST":
        Feedback.objects.create(**feedback_data)
        del request.session["feedback_data"]
        return redirect("sandbox:index")

    form = FeedbackForm(initial=feedback_data)
    return render(request, "sandbox/feedback_review.html", {"form": form})


class SpecifcRecipesView(View):
    def get(self, request, *args, **kwargs):
        # fetch recipes with "refreshing" in the description
        refreshing_recipes = Recipe.objects.filter(description__icontains="rich")
        context = {"refreshing": refreshing_recipes}
        return render(request, "sandbox/refreshing_recipes.html", context)
