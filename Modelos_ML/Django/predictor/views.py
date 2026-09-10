from django.conf import settings
from django.shortcuts import render


def index(request):
    """Sirve la página del predictor. El formulario llama a la API de
    Regresión Lineal (FastAPI, desplegada en Railway) directamente desde
    el navegador vía fetch — Django solo entrega la plantilla, y le pasa
    la URL de la API leída de settings.API_BASE_URL (variable de entorno)."""
    return render(request, 'predictor/index.html', {
        'api_base_url': settings.API_BASE_URL,
    })
