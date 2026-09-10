from django.shortcuts import render


def index(request):
    """Sirve la página del predictor. El formulario llama a la API de
    Regresión Lineal (FastAPI, desplegada en Railway) directamente desde
    el navegador vía fetch — Django solo entrega la plantilla."""
    return render(request, 'predictor/index.html')
