from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def contacto(request):
    return render(request, 'core/contacto.html')

def comprar(request):
    return render(request, 'core/comprar.html')

def servicios(request):
    return render(request, 'core/servicios.html')