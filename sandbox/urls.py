from django.urls import path
from . import views

app_name = "sandbox"
# https://mysite.com/
urlpatterns = [path("", views.index)]
