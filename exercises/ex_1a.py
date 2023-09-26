# El codigo te crea una imagen con la traza de un electro con el  tiempo 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter 

# Datos iniciales
Vi = 3e6        # m/s
E = 400         # N/C
Tt = 3000e-9    # Tiempo total
dt = 100e-9     # Intervalo de tiempo

# Calculamos la aceleración debida al campo eléctrico (F = q * E)
q = -1.602e-19          # Carga del electrón en C
a = q * E / 9.109e-31  # Masa del electrón en kg

# Calculamos la velocidad final
Vf = Vi + a * Tt

# Calculamos los tiempos
tiempos = np.arange(0, Tt + dt, dt)

# Calculamos las posiciones usando la ecuación de movimiento
y = 0.5 * a * tiempos**2 + Vi * tiempos
x = Vi * tiempos

# Crear figura
fig, ax = plt.subplots()
line, = ax.plot(x,y, "ro")

ax.set_title("Traza del movimiento del electron con el tiempo")
ax.set_xlabel("Posicion X")
ax.set_ylabel("Posicion Y")
ax.grid()
plt.tight_layout()
ax.autoscale(enable=True, axis='both', tight=True)

# Mostrar la figura
plt.show()
