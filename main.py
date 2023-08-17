import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c,max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2]))

def display(xmin,xmax,ymin,ymax,width=10,height=10,max_iter=256):
    dpi = 80
    img_width = dpi * width
    img_height = dpi * height
    x,y,z = mandelbrot_set(xmin,xmax,ymin,ymax,img_width,img_height,max_iter)
    
    fig, ax = plt.subplots(figsize=(width, height),dpi=dpi)
    ticks = np.arange(0,img_width,3*dpi)
    x_ticks = xmin + (xmax-xmin)*ticks/img_width
    plt.xticks(ticks, x_ticks)
    y_ticks = ymin + (ymax-ymin)*ticks/img_width
    plt.yticks(ticks, y_ticks)
    ax.set_title("Mandelbrot Set")
    ax.imshow(z, origin='lower', cmap='hot', extent=(xmin, xmax, ymin, ymax))
    plt.show()

# Set the parameters and visualize
display(-2.0, 0.7, -1.35, 1.35, width=10, height=10)
