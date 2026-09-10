import os
import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="API de Regresión Lineal", description="API para predecir precios de viviendas usando un modelo de regresión lineal entrenado.", version="1.0.0")

# Permite que el frontend (servido desde otro origen: un archivo local,
# Netlify, Vercel, etc.) pueda llamar a esta API desde el navegador.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta relativa a la ubicación de este script, sin importar desde dónde se ejecute
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "linear_model.joblib")
STATIC_DIR = os.path.join(BASE_DIR, "static")

try:
    # Load the trained model
    model = joblib.load(MODEL_PATH)
except Exception:
    model = None

class housem2(BaseModel):
    area_m2: float = Field(..., description="Área de la vivienda en metros cuadrados", examples=[82.5])

@app.get("/", include_in_schema=False)
def serve_frontend():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

@app.get("/api/health")
def health_check():
    return {"status": "OK", "message": "API de Regresión Lineal está funcionando correctamente.", "model_loaded": model is not None}

@app.post("/predict")
def predict_price(data: housem2):
    if model is None:
        raise HTTPException(status_code=500, detail="Modelo no disponible. Intente nuevamente más tarde.")

    predicted_price = model.predict([[data.area_m2]])
    return {
        "area_m2": data.area_m2,
        "predicted_price": round(float(predicted_price[0]), 2)
    }