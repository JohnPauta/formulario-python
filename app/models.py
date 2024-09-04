from django.db import models

class Usuario(models.Model):
    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=100)
    apellido_p = models.CharField(max_length=100)
    apellido_m = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono_movil = models.CharField(max_length=15)
    cuenta_bancaria = models.CharField(max_length=20)
    curso = models.CharField(max_length=100)
