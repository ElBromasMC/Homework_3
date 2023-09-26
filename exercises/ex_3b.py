import numpy as np
import matplotlib.pyplot as plt

# Constants
K = 9e+9

class Particle():
    def __init__(self, position, charge):
        self.position = position
        self.charge = charge

    def getXField(self, position):
        return K*self.charge*(position[0]-self.position[0])/np.sqrt((position[0]-self.position[0])**2 + (position[1]-self.position[1])**2)**3
    
    def getYField(self, position):
        return K*self.charge*(position[1]-self.position[1])/np.sqrt((position[0]-self.position[0])**2 + (position[1]-self.position[1])**2)**3


# Define the particles
particles = [ Particle((-1, -1), 3e-6)
            , Particle((1, 1), 3e-6)
            , Particle((1, -1), -3e-6)
            , Particle((-1, 1), -3e-6)
            ]



def ex_3a():
    # Domain of the vector field
    x, y = np.meshgrid(np.linspace(-5, +5, 30), np.linspace(-5, +5, 30))
    # The vector field
    u, v = 0, 0

    for particle in particles:
        u += particle.getXField((x,y))
        v += particle.getYField((x,y))

        # Plot the particles
        plt.plot(particle.position[0], particle.position[1], 'ro', markersize=20)

    # Plot the function via streamplot
    plt.streamplot(x, y, u, v)
    plt.title('Ejercicio 3b')
    plt.grid(True)
    plt.gca().set_aspect('equal')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3a()
