from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Bienvenue à Nuit de l'Info!</h1>")

def about(request):
    return HttpResponse("<h1>À propos de Nuit de l'Info</h1>")

