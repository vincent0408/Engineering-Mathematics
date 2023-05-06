import math
import numpy as np
import matplotlib.pyplot as plt

def problem_a():
    delta_x = .02
    N = int(4 / delta_x) - 1
    half = (N - 1) // 2
    def gx(x):
        return np.sin(math.pi * (x-2) ** 3 / 8)
    f = np.arange(-half, half+1, 1) / delta_x / N
    gdn = gx(np.arange(0 + delta_x, 4, delta_x))
    gdm = np.roll(np.fft.fft(gdn)* delta_x, (N - 1) // 2) * np.exp(4j * math.pi * f)

    plt.plot(f, gdm.real, 'o-')
    plt.plot(f, gdm.imag, 'o-')

    plt.show()
    
def problem_d():
    delta_x = .05
    def gx(x):
        return (x - 3) * np.exp(-np.abs((x - 3)) ** (3 / 2))
    N = int(6 / delta_x) - 1
    half = (N - 1) // 2
    f = np.arange(-half, half+1, 1) / delta_x / N
    
    gdn = gx(np.arange(0+ delta_x, 6, delta_x))
    gdm = np.roll(np.fft.fft(gdn)* delta_x, (N - 1) // 2) * np.exp(6j * math.pi * f)
    plt.plot(f, gdm.real, 'o-')
    plt.plot(f, gdm.imag, 'o-')
    plt.show()

    
def test():
    delta_x = .1
    N = int(2 / delta_x) + 1
    half = (N - 1) // 2
    def gx(x):
        return (1 - np.abs((x - 1))) ** 2
    f = np.arange(-half, half + 1, 1) / delta_x / N  
    gdn = gx(np.arange(0, 2+delta_x,delta_x))
    gdm = np.roll(np.fft.fft(gdn)* delta_x, (N - 1) // 2) * np.exp(2j * math.pi * f)
    plt.plot(f, gdm.real, 'o-')
    plt.plot(f, [0] * N)
    plt.show()

# test()  
problem_a()
problem_d()