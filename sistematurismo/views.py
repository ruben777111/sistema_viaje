from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
def inicio(request):
    return render(request,'paginas/inicio.html')

# Create your views here.
