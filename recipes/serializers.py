from rest_framework import serializers
from .models import Recipe, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class RecipeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    favorited_by = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        # fields = "__all__"
        fields = [
            "id",
            "name",
            "description",
            "ingredients",
            "directions",
            "date_added",
            "category",
            "user",
            "image",
            "favorited_by",
        ]
        read_only_fields = ["image"]
