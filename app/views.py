from django.shortcuts import render
from .forms import ComprobarCedulaForm, RegisterUsuarioForm

def index(request):
    return render(request, 'index.html')

def comprobar_cedula(request):
    if request.method == 'POST':
        form = ComprobarCedulaForm(request.POST)
        if form.is_valid():
            # Procesar la cédula
            pass
    else:
        form = ComprobarCedulaForm()
    return render(request, 'comprobar_cedula.html', {'form': form})

def register_usuario(request):
    if request.method == 'POST':
        form = RegisterUsuarioForm(request.POST)
        if form.is_valid():
            # Procesar el registro del usuario
            pass
    else:
        form = RegisterUsuarioForm()
    return render(request, 'register_usuario.html', {'form': form})
