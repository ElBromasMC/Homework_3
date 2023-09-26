import numpy as np
import matplotlib.pyplot as plt

# Variables
# Position of the particle
a, b = 3, 2

# Charge of the particle
q = -3e-6


# Constants
K = 9e+9



def ex_3a():
    # Domain of the vector field
    x, y = np.meshgrid(np.linspace(-5, +5, 30), np.linspace(-5, +5, 30))
    # The vector field
    u, v = K*q*(x-a)/np.sqrt((x-a)**2 + (y-b)**2)**3, K*q*(y-b)/np.sqrt((x-a)**2 + (y-b)**2)**3

    # Plot the particle
    plt.plot(a, b, 'ro', markersize=20)

    # Plot the function via streamplot
    plt.streamplot(x, y, u, v)
    plt.title('Ejercicio 3a')
    plt.grid(True)
    plt.gca().set_aspect('equal')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3a()
