from django.urls import path
from recipes.views import pag_home


urlpatterns = [
    path("", pag_home),
]
