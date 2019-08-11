from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    context = {
        "email": "edipoelwes2@gmail.com",

    }
    return render(request, "home.html", context)

def contato(request):
    context = {
        "email": "edipoelwes2@gmail.com",
        "nomes": ["edipo", "jessianne", "Joao"]
    }
    return render(request, "contato.html", context)

def Novidade_datalhes(request):
    context = {
        "email": "edipoelwes2@gmail.com",
        "nomes": ["edipo", "jessianne", "Joao"]
    }
    return render(request, "Novidade_detalhes.html", context)
