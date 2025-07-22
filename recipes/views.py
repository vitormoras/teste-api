from django.shortcuts import render


def pag_home(request):
    return render(
        request,
        "recipes/home.html",
        context={"name": "Vitor"},
    )
