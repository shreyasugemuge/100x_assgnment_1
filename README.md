# Animated Mandelbrot Set Visualization

This Python script animates a zoom into the Mandelbrot set to create a "trippy" effect. It uses the `matplotlib` library to animate a zoom into the Mandelbrot set while applying a pseudo-3D rotation effect that gives a cylindrical projection appearance.

## Requirements

- Python 3.x
- Matplotlib
- Numpy

## Installation

First, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

After installing Python, you need to install the required Python packages. Open your terminal and run the following command:

```bash
pip install matplotlib numpy
```

## Usage

To run the script, save it as `animated_mandelbrot.py` and execute the following command in your terminal:

```bash
python animated_mandelbrot.py
```

This will open a window displaying the animated Mandelbrot set. 

## Customization

You can adjust the speed of the zoom, the point into which the animation zooms, and the 3D effect by modifying the following variables in the `animated_mandelbrot.py` script:

- `zoom_factor`: Determines the speed of the zoom.
- `focus_x` and `focus_y`: Determine the coordinates into which you want to zoom.
- `MAX_ITER`: Determines the maximum number of iterations for the Mandelbrot calculation, which affects the level of detail.

## Example

The default script animates the Mandelbrot set by zooming into the point `(-0.7, 0.0)` with a 3D rotation effect.

