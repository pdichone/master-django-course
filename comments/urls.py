from django.urls import include, path

from comments import views


app_name = "comments"
urlpatterns = [path("", views.comments)]
