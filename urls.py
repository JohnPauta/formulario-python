# urls.py
from django.urls import path
from app import views  # Importa el módulo views completo

urlpatterns = [
    path('', views.index, name='index'),

    path('verify/', views.verify_cedula, name='verify_cedula'),

    path('submit/', views.submit_data, name='submit_data'),

    path('comprobante/', views.submit_data, name='submit_comprobante'),
]