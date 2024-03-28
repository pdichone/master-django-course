from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")


# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
