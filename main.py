import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create the Mandelbrot fractal
def mandelbrot(c,max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2]))

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('off')

# Initial frame settings
XMIN, XMAX, YMIN, YMAX = -2.0, 0.7, -1.35, 1.35
WIDTH, HEIGHT = 800, 800
MAX_ITER = 256

x, y, z = mandelbrot_set(XMIN, XMAX, YMIN, YMAX, WIDTH, HEIGHT, MAX_ITER)
im = ax.imshow(z, origin='lower', cmap='hot', extent=(XMIN, XMAX, YMIN, YMAX), animated=True)

def update(frame):
    global XMIN, XMAX, YMIN, YMAX
    zoom_factor = 1.04  # Determines the speed of zoom

    # Adjust these to determine where you want to zoom into
    focus_x = -0.7
    focus_y = 0.0

    # Compute new bounds
    XMIN = (XMIN - focus_x) / zoom_factor + focus_x
    XMAX = (XMAX - focus_x) / zoom_factor + focus_x
    YMIN = (YMIN - focus_y) / zoom_factor + focus_y
    YMAX = (YMAX - focus_y) / zoom_factor + focus_y
    
    x, y, z = mandelbrot_set(XMIN, XMAX, YMIN, YMAX, WIDTH, HEIGHT, MAX_ITER)

    # 3D rotation illusion effect
    y_range = np.linspace(YMIN, YMAX, HEIGHT)
    y_range = np.sin(y_range * np.pi)
    z = z * y_range[:, np.newaxis]

    im.set_array(z)
    im.set_extent((XMIN, XMAX, YMIN, YMAX))
    return [im]

ani = FuncAnimation(fig, update, frames=200, blit=True, interval=50)  # 200 frames with 50ms interval
plt.show()
