from django.shortcuts import render
from django.template import loader

def profil(request):
    return render(request, 'indexprofil.html')
