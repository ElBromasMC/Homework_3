import numpy as np
import math

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

def calcXField(position, particles):
    state = 0
    for particle in particles:
        state += particle.getXField(position)
    return state

def calcYField(position, particles):
    state = 0
    for particle in particles:
        state += particle.getYField(position)
    return state

def safeIntInput(str, pred=lambda _: True) -> int:
    try:
        n = int(input(str))
        if pred(n):
            return n
        else:
            print("\033[91mInvalid value!\033[0m")
            return safeIntInput(str, pred)
    except:
        print("\033[91mParse error! Please enter again.\033[0m")
        return safeIntInput(str, pred)

def safeFloatInput(str, pred=lambda _: True) -> int:
    try:
        n = float(input(str))
        if pred(n):
            return n
        else:
            print("\033[91mInvalid value!\033[0m")
            return safeFloatInput(str, pred)
    except:
        print("\033[91mParse error! Please enter again.\033[0m")
        return safeFloatInput(str, pred)

if __name__ == "__main__":
    particles = []
    # Number of particles
    n = safeIntInput("Enter the number of particles: ", lambda x: x > 0)
    
    print("\n\033[1mYou can use scientific notation! ex. 3e-6\033[0m")
    for i in range(n):
        particle = Particle((safeFloatInput("\nEnter the X-coordinate for the particle: "),
                             safeFloatInput("Enter the Y-coordinate for the particle: ")),
                            safeFloatInput("Enter the electric charge for the particle: "))
        particles.append(particle)

    # Position
    print("\nEnter the coordinate where you want to calculate the Electric Field")
    position = (safeFloatInput("Enter the X-coordinate: "), safeFloatInput("Enter the Y-coordinate: "))

    # Calculate the field on the given point
    FieldX = calcXField(position, particles)
    FieldY = calcYField(position, particles)

    Module = np.sqrt(FieldX**2 + FieldY**2)

    # Print the vector
    print("\nThe electric field in ({:.2f}, {:.2f}) is ({:.2f}, {:.2f})".format(position[0], position[1], FieldX, FieldY))

    # Print the module of the vector
    print("It's module is {:.2f}".format(Module))

    # Print the angle with the X axis
    print("It's angle with the X axis is {:.2f}".format(np.degrees(np.arccos(FieldX/Module))))



