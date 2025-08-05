from django.shortcuts import render


def pag_home(request):
    return render(
        request,
        "recipes/pages/home.html",
        context={"name": "Vitor"},
    )


def pag_recipe(request, id):
    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={"name": "Vitor"},
    )
