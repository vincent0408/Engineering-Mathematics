import math
import numpy as np
import matplotlib.pyplot as plt

def problem_a():
    dx = 0.02
    x = np.arange(0, 4 - dx, dx)
    N = len(x)
    half = N // 2
    def gx(x):
        return np.sin(math.pi * x ** 3 / 8)
    gdn = gx(x - 1.98)
    r = np.fft.fft(gdn)
    gdm = np.roll(np.fft.fft(gdn) * dx, half)
    f = np.arange(N) / dx / N
    f = np.concatenate((f[-half:] - 1/ dx, f[:-half]))
    res = gdm * np.exp(1j * 2 * 1.98 * math.pi * f)
    plt.figure(figsize=(20, 6)), plt.plot(f, res.real), plt.plot(f, res.imag), plt.show()    

    
def problem_d():
    dx = 0.05
    x = np.arange(0, 6 - dx, dx)
    N = len(x)
    half = N // 2
    def gx(x):
        return x * np.exp(-np.abs(x) ** (3 / 2))
    gdn = gx(x - 2.95)
    gdm = np.roll(np.fft.fft(gdn) * dx, half)
    f = np.arange(N) / dx / N
    f = np.concatenate((f[-half:] - 1/ dx, f[:-half]))
    res = gdm * np.exp(1j * 2 * 2.95 * math.pi * f)
    plt.figure(figsize=(20, 6)), plt.plot(f, res.real), plt.plot(f, res.imag), plt.show()    

problem_a()
problem_d()