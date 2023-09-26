import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
Xf = Vi * Tt

# Crear figura
fig, ax = plt.subplots()
ax.set_xlim(0, Xf)
ax.set_ylim(-300,0)      # Rango en el eje y

circle, = ax.plot([], [], 'ro', markersize=8)  # Usamos 'ro' para un círculo rojo
title = ax.set_title("")  # Inicialmente, el título está vacío
ax.set_xlabel("Posición X")
ax.set_ylabel("Posicion Y")
ax.grid()

# Función de inicialización
def init():
    circle.set_data([], [])
    return circle,

# Función de animación
def animate(i):
    x = Vi*tiempos[i]  # Obtenemos la posición en x en el tiempo actual
    y_data = y[i]   # Obtenemos la posición en y en el tiempo actual
    circle.set_data(x, y_data)
    title.set_text(f"Posición en (x,y) = ({x:.2f} ,{y_data:.2f}) ")
    

# Crear la animación
ani = FuncAnimation(fig, animate, init_func=init, frames=len(tiempos), interval=50, blit=False)

# Crear la animación en formato MP4
ani.save('electron_animation.mp4', fps=10)

# Mostrar la figura
plt.show()
