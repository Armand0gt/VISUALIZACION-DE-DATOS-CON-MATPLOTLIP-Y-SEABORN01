import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parámetros
num_plantas = 1200
dist_planta_hilera = 55  # cm
dist_planta_planta = 40  # cm
num_surcos = num_plantas // (dist_planta_hilera // dist_planta_planta)  # Corregido: uso de doble barra para división entera

# Generar datos aleatorios para plantas afectadas (1) y sanas (0)
np.random.seed(42)
plantas_afectadas = np.random.choice([0, 1], size=num_plantas, p=[0.8, 0.2])

# Crear DataFrame con coordenadas de las plantas
coordenadas_x = np.arange(0, num_surcos) * dist_planta_hilera
coordenadas_y = np.arange(0, num_plantas // num_surcos) * dist_planta_planta
coordenadas = [(x, y) for x in coordenadas_x for y in coordenadas_y]
df = pd.DataFrame(coordenadas, columns=['x', 'y'])
df['afectada'] = plantas_afectadas

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(10, 6))


# Dibujar surcos (líneas verticales)
for x in coordenadas_x:
    ax.axvline(x, color='gray', linestyle='--', alpha=0.5)

# Dibujar plantas afectadas (puntos rojos)
ax.scatter(df[df['afectada'] == 1]['x'], df[df['afectada'] == 1]['y'], color='red', label='Plantas afectadas')

# Dibujar plantas sanas (puntos verdes)
ax.scatter(df[df['afectada'] == 0]['x'], df[df['afectada'] == 0]['y'], color='green', label='Plantas sanas')

# Configurar ejes y leyenda
ax.set_xlabel('Distancia entre hileras (cm)')
ax.set_ylabel('Distancia entre plantas (cm)')
ax.set_title('Mapa de calor de plantas de tomate')
ax.legend()

# Mostrar el número de surcos y plantas afectadas
print(f"Número de surcos: {num_surcos}")
print(f"Plantas afectadas: {plantas_afectadas.sum()}")
print(f"Plantas sanas: {num_plantas - plantas_afectadas.sum()}")

# Mostrar el gráfico
plt.show()

