from os import name

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "global/home.html", context={
        "name": "Pedro Augusto",
    })


def contato(request):
    return render(request, 'me_apague/temp.hmtl')


def sobre(request):
    return HttpResponse("sobre")
