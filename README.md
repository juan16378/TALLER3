# Taller 3 — Machine Learning con Python

Dos modelos de ML expuestos como aplicaciones web: diagnóstico clínico y predicción de precio de vivienda.

## 🚀 Despliegues

| Proyecto | Link |
|---|---|
| 🩺 Diagnóstico Clínico (Streamlit) | [taller3git-nuttk6ohkssmvddozcijtz.streamlit.app](https://taller3git-nuttk6ohkssmvddozcijtz.streamlit.app/) |
| ⚙️ API Regresión Lineal (FastAPI) | [taller3-production-b558.up.railway.app](https://taller3-production-b558.up.railway.app/) |
| 🖥️ Frontend Regresión Lineal (Django) | [frontend-production-e6e5c.up.railway.app](https://frontend-production-e6e5c.up.railway.app/) |

[![Streamlit](https://img.shields.io/badge/Streamlit-Demo-FF4B4B?logo=streamlit&logoColor=white)](https://taller3git-nuttk6ohkssmvddozcijtz.streamlit.app/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)](https://taller3-production-b558.up.railway.app/)
[![Django](https://img.shields.io/badge/Frontend-Django-092E20?logo=django&logoColor=white)](https://frontend-production-e6e5c.up.railway.app/)

## 📂 Estructura

```
carga_datos/            # Notebooks de carga de datos (CSV, Excel, API, web scraping)
Modelos_ML/
├── RamdomForest/        # Diagnóstico clínico (RandomForest + Streamlit)
│   └── RegresionLineal/ # Precio de vivienda (FastAPI + Django)
│       ├── back/        # API (FastAPI)
│       └── front/       # Frontend standalone (HTML)
└── Django/              # Frontend Django (consume la API)
```

## 🛠️ Stack

Python · scikit-learn · pandas · FastAPI · Django · Streamlit · Docker · Railway

## ⚙️ Local

```bash
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
```

- **Streamlit**: `streamlit run Modelos_ML/RamdomForest/3.Predecir_enefermedad.py`
- **API**: `uvicorn main:app --reload` (desde `back/`)
- **Django**: `python manage.py runserver` (desde `Modelos_ML/Django/`)

## 👤 Autor

Juan José Monsalve
