from django.shortcuts import render


def pag_home(request):
    return render(
        request,
        "recipes/pages/home.html",
        context={"name": "Vitor"},
    )
