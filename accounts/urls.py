from django.urls import path, include
from .views import register
from accounts import views

app_name = "accounts"
urlpatterns = [
    path("register/", register, name="register"),
    path("", include("django.contrib.auth.urls")),
    path("edit-profile/", views.edit_user_profile, name="edit_user_profile"),
]
