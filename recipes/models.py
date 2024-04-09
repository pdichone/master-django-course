from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from foodie_app.models import Category


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField()
    directions = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="recipes"
    )
    image = models.ImageField(upload_to="recipe_images/", null=True, blank=True)
    favorited_by = models.ManyToManyField(User, related_name="favorite_recipes", blank=True)
    
    def get_absolute_url(self):
        return reverse("recipes:recipe_detail", args=[str(self.id)])

    def __str__(self):
        return self.name
