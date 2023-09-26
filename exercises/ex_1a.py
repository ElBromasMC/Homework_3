import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter 

# Variables in SI
E  = (0, 400)

v0 = (3e+6, 0)
q = -1.6e-19
m = 9.1e-31

t0 = 0
tf = 3000e-9 
dt = 100e-9

# Domain of time
t = np.arange(t0, tf + dt, dt)

# Equation of motion
def motion(t):
    return v0[0]*t + E[0]*q*t**2/(2*m), v0[1]*t + E[1]*q*t**2/(2*m)

x, y = motion(t)

# Plot the motion
fig, ax = plt.subplots()
particle = ax.plot(x,y, "bo")[0]

ax.set_title("Particle's motion")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid()
ax.autoscale(enable=True, axis='both')

# Display the plot
plt.show()
