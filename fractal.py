import matplotlib.pyplot as plt
import numpy as np
from numba import jit


@jit(nopython=True, cache=False)
def mandelbrot(c: complex, maxiter: int) -> complex:
    z = 0j
    for i in range(maxiter):
        # za = abs(z.real) + abs(z.imag) * 1j
        # z = za * za + c
        z = z * z + c

        if abs(z) > 2:
            return i
    return maxiter


if __name__ == "__main__":
    xx = np.linspace(-2, 2, 10000)
    yy = np.linspace(-2, 2, 10000)
    maxiter = 100

    histr = []
    histi = []
    for x in xx:
        for y in yy:
            c = x + y * 1j
            if mandelbrot(c, maxiter) == maxiter:
                histr.append(c.real)
                histi.append(c.imag)
    plt.scatter(histr, histi, c="blue", s=0.1)

    plt.show()
