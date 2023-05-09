import math
import numpy as np
import matplotlib.pyplot as plt

def problem_a():
    dx = 0.02
    x = np.arange(dx, 4, dx)
    N = len(x)
    half = N // 2
    def gx(x):
        return np.sin(math.pi * x ** 3 / 8)
    gdn = gx(x - 2)
    gdm = np.roll(np.fft.fft(gdn) * dx, half)
    f = np.arange(N) / dx / N
    f = np.concatenate((f[-half:] - 1/ dx, f[:-half]))
    res = gdm * np.exp(1j * 2 * 2 * math.pi * f)
    plt.plot(f, res.real), plt.plot(f, res.imag), plt.show()    

    
def problem_d():
    dx = 0.05
    x = np.arange(dx, 6, dx)
    N = len(x)
    half = N // 2
    def gx(x):
        return x * np.exp(-np.abs(x) ** (3 / 2))
    gdn = gx(x - 3)
    gdm = np.roll(np.fft.fft(gdn) * dx, half)
    f = np.arange(N) / dx / N
    f = np.concatenate((f[-half:] - 1/ dx, f[:-half]))
    res = gdm * np.exp(1j * 2 * 3 * math.pi * f)
    plt.plot(f, res.real), plt.plot(f, res.imag), plt.show()    

    
def test():
    dx = 0.1
    x = np.arange(0, 2+dx, dx)
    N = len(x)
    half = N // 2
    def gx(x):
        return (1 - np.abs(x)) ** 2
    gdn = gx(x - 1)
    gdm = np.roll(np.fft.fft(gdn) * dx, half)
    f = np.arange(N) / dx / N
    f = np.concatenate((f[-half:] - 1/ dx, f[:-half]))
    res = gdm * np.exp(1j * 2 * math.pi *f)
    plt.plot(f, res.real), plt.plot(f, res.imag), plt.show()


# test()  
problem_a()
problem_d()