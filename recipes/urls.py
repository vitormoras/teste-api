from django.urls import path
from . import views


urlpatterns = [
    path("", views.pag_home),
    path("recipes/<int:id>/", views.pag_recipe),
]
