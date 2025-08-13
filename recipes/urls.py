from django.urls import path
from . import views


app_name = "recipes"

urlpatterns = [
    path("", views.pag_home, name="home"),
    path("recipes/<int:id>/", views.pag_recipe, name="info"),
]
