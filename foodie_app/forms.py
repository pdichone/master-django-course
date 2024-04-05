from django import forms

from foodie_app.models import Category
from recipes.models import Recipe


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        # labels = {"name": "Category Name"}
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Category name",
                }
            )
        }


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "name",
            "description",
            "ingredients",
            "directions",
            "category",
            "image",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Recipe title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Description",
                    "rows": "5",
                }
            ),
            "ingredients": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingredients",
                    "rows": "5",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
