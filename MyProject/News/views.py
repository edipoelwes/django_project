from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("<h1>Pagina Home ou index</h1>")

def contato(request):
    return HttpResponse("<h1>Pagina de contatos</h1>")

