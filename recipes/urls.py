from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path("", home),
    path("contato/", sobre),
    path("sobre/", contato),
]
