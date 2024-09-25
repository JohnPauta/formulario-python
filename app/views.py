import json
import requests
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    if request.method == "POST":
        try:
            json_datos = {
                "a": "registrarinscripcion",
                "key": "fd3569c8-f83f-49a9-8612-9227c9b93104",
                "cedula": request.POST["estudiante[cedula]"],
                "nombres": request.POST["estudiante[nombres]"],
                "apellido1": request.POST["estudiante[apellido1]"],
                "apellido2": request.POST["estudiante[apellido2]"],
                "emailinstitucional": request.POST["estudiante[emailinstitucional]"],
                "email": request.POST["estudiante[email]"],
                "sexo": request.POST["estudiante[sexo]"],
                "fechanacimiento": request.POST["estudiante[fechanacimiento]"],
                "telefono_movil": request.POST["estudiante[telefono_movil]"],
                "telefono_fijo": request.POST["estudiante[telefono_fijo]"],
                "direccion": request.POST["estudiante[direccion]"],
                "malla": request.POST["estudiante[malla]"],
                "coordinacion": request.POST["estudiante[coordinacion]"],
                "sesion": request.POST["estudiante[sesion]"],
                "habilitado": request.POST["estudiante[habilitado]"],
            }
            respuesta = requests.post("https://sga.isteps.edu.ec/api", data=json_datos, timeout=10)
            datosrespuesta = json.loads(respuesta.content)
            if datosrespuesta["result"] == "ok":
                return JsonResponse({"success": True})
            return JsonResponse({"success": False, "message": "Error en creacion del estudiante"})
        except request.exceptions.RequestException as ex:
            print(ex)
            return JsonResponse(
                {"success": False, "message": "Excepcion: Error en creacion del estudiante"}
            )
    else:
        return render(request, "registro.html")


def verify_cedula(request):
    if request.method == "POST":
        cedula = request.POST.get("cedula")
        # Aquí iría la lógica para verificar la cédula
        return JsonResponse({"success": True, "message": "Cédula verificada"})


def submit_data(request):
    if request.method == "POST":
        data = request.POST
        # Aquí iría la lógica para enviar los datos al SGA
        return JsonResponse(
            {"success": True, "message": "Datos del estudiante enviados al SGA"}
        )


def submit_comprobante(request):
    if request.method == "POST":
        data = request.POST
        # Aquí iría la lógica para enviar los datos al SGA
        return JsonResponse(
            {"success": True, "message": "Datos del comprobante enviados al SGA"}
        )
