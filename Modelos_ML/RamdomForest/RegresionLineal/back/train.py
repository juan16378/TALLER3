import os
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODELS_DIR, exist_ok=True)

# Generate some sample data
X = np.array([[40], [50], [60], [85], [100],[120]])
y = np.array([210000000, 300000000, 350000000, 500000000, 600000000, 700000000])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# #Predicciones de prueba
# y_pred = model.predict(X)

# #Imprimir la informacion del modelo entrenado
# print("Coeficiente:", model.coef_[0])
# print("Termino independiente:", model.intercept_)

# #Graficar datos reales
# plt.scatter(X, y, color='red', label='Datos de entrenamiento')

# #Graficar los datos de entrenamineto y la linea de regresion
# plt.plot(X, y_pred, color='blue', label='Línea de regresión')

# plt.xlabel("Superficie (m2)")
# plt.ylabel("Precio (COP)")
# plt.title("Regresión Lineal")
# plt.legend()
# plt.grid(True)

# plt.show()

# Save the trained model
joblib.dump(model, os.path.join(MODELS_DIR, "linear_model.joblib"))