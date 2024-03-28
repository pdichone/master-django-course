from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")
    search_fields = ["name"]


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_added")


# Register your models here.
admin.site.register(Category, CategoryAdmin)
