from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField()
    directions = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
