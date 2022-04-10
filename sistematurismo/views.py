from django.shortcuts import render
from django.http import HttpResponse
from .models import cliente
def inicio(request):
    return render(request,'paginas/inicio.html')

def cliente(request):
    return render(request,'cliente/contenidocliente.html')


# Create your views here.
