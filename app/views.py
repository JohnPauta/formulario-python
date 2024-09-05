# views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ComprobarCedulaForm, RegisterUsuarioForm
from datetime import datetime

def index(request):
    return render(request, 'registro.html')

def verify_cedula(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        # Aquí iría la lógica para verificar la cédula
        return JsonResponse({'success': True, 'message': 'Cédula verificada'})

def submit_data(request):
    if request.method == 'POST':
        data = request.POST
        # Aquí iría la lógica para enviar los datos al SGA
        return JsonResponse({'success': True, 'message': 'Datos del estudiante enviados al SGA'})

def submit_comprobante(request):
    if request.method == 'POST':
        data = request.POST
        # Aquí iría la lógica para enviar los datos al SGA
        return JsonResponse({'success': True, 'message': 'Datos del comprobante enviados al SGA'})
