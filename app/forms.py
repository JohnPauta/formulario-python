from django import forms

class ComprobarCedulaForm(forms.Form):
    user_cedula = forms.CharField(label='Cédula', max_length=10, required=True)

class RegisterUsuarioForm(forms.Form):
    user_nombres = forms.CharField(label='Nombres', max_length=100, required=True, disabled=True)
    user_apellido_p = forms.CharField(label='Apellido Paterno', max_length=100, required=True, disabled=True)
    user_apellido_m = forms.CharField(label='Apellido Materno', max_length=100, required=True, disabled=True)
    user_correo = forms.EmailField(label='Correo', required=True, disabled=True)
    user_telefono_Movil = forms.CharField(label='Teléfono Móvil', max_length=15, required=True, disabled=True)
