from django.shortcuts import render
from django.http import HttpResponse
from .models import Tatuaje, Diseno
from .form import ContactoForm

# Create your views here.

def inicio(request):
    tatuajes = Tatuaje.objects.all()
    diseno = Diseno.objects.all()
    data = {
        "tatuajes": tatuajes,
        "diseno": diseno
    }
    return render(request, 'paginas/index.html', data)

def diseno(request):
    diseno = Diseno.objects.all()
    data = {
        "diseno": diseno
    }
    return render(request, 'paginas/diseños.html', data)

def tatuajes(request):
    tatuajes = Tatuaje.objects.all()
    data = {
        "tatuajes": tatuajes
    }
    return render(request, 'paginas/tatuajes.html', data)

def contacto(request):
    data = {
        "form": ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"] = formulario
    return render(request, 'paginas/formulario.html', data)

def ayuda(request):
    return render(request, 'paginas/ayuda.html')

def about(request):
    return render(request, 'paginas/about.html')