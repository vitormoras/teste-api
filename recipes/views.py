from django.shortcuts import render
from utils.recipes.factory import make_recipe


def pag_home(request):
    return render(
        request,
        "recipes/pages/home.html",
        context={"recipes": [make_recipe() for _ in range(10)]},
    )


def pag_recipe(request, id):
    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={
            "recipe": make_recipe(),
            "is_datail_page": True,
        },
    )
