from django.urls import path
from . import views


urlpatterns = [
    path("", views.pag_home, name="recipes-home"),
    path("recipes/<int:id>/", views.pag_recipe, name="recipes-info"),
]
