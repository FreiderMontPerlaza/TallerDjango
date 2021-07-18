from django.http import request
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app/home.html')


def galeria(request):
    return render(request,'app/galeria.html')

def contacto(request):
    return render(request,'app/contacto.html')

def manualidades(request):
    return render(request,'app/manualidades.html')


def escultura(request):
    return render(request,'app/escultura.html') 

def pintura(request):
    return render(request,'app/pintura.html')

def artista(request):
    return render(request,'app/artista.html')

