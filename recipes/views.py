from django.shortcuts import render
from django.http import HttpResponse


def pag_home(request):
    return render(
        request,
        "recipes/home.html",
        context={"name": "Vitor"},
    )


def pag_contato(request):
    return HttpResponse("Essa é nossa página que se refere ao nossos contatos!")


def pag_sobre(request):
    return HttpResponse(
        "Agora temos um pouco sobre oque somos, desfrute dessa magnifica página!"
    )
