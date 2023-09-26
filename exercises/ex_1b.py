import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Variables in SI
E  = (0, 400)

v0 = (3e+6, 0)
q = -1.6e-19
m = 9.1e-31

t0 = 0
tf = 3000e-9 
dt = 3e-8

# Calculate the number of frames
num_frames = int((tf - t0) / dt) + 1

# Equation of motion
def motion(t):
    return v0[0]*t + E[0]*q*t**2/(2*m), v0[1]*t + E[1]*q*t**2/(2*m)

# Plot the particle
fig, ax = plt.subplots()
ax.set_title("Particles's motion")
ax.set_xlim(motion(t0)[0], motion(tf)[0])
ax.set_ylim(motion(tf)[1], motion(t0)[1])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.autoscale(enable=True, axis='both')
ax.grid()

particle = ax.plot([], [], 'bo')[0]
info_text = ax.text(0.1, 0.8, '', transform=ax.transAxes)



def init():
    particle.set_data([], [])
    info_text.set_text('')
    return particle,

def animate(t):
    x, y = motion(t)
    particle.set_data(x, y)
    info_text.set_text(f'Time: {t:.2e}s\nPosition: ({x:.2f}, {y:.2f})')
    return particle, info_text

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(t0, tf, num_frames), init_func=init, blit=True, interval=1)

# Save the animation as gif
# ani.save('particle_motion.gif', writer=PillowWriter(fps=30))

# Display the animation
plt.show()
