from django.urls import path
from recipes.views import pag_home, pag_contato, pag_sobre


urlpatterns = [
    path("", pag_home),
    path("sobre/", pag_sobre),
    path("contato/", pag_contato),
]
