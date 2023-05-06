import math
import numpy as np
import matplotlib.pyplot as plt

def problem_a():
    delta_x = .02
    N = int(4 / delta_x) - 1
    half = (N - 1) // 2
    def gx(x):
        return np.sin(math.pi * (x-2) ** 3 / 8)
    gdn = gx(np.arange(0 + delta_x, 4, delta_x))
    # plt.plot(np.arange(0 + delta_x, 4, delta_x), gdn)
    # plt.show()
    gdm = np.fft.fft(gdn)
    # plt.stem(np.arange(0, 201, 1), gdm, markerfmt=' ', linefmt='r-', label='imag')
    # plt.show()
    f = np.arange(-half, half+1, 1) / delta_x / N
    gdm_real = np.roll(gdm.real, half) * delta_x
    gdm_imag = np.roll(gdm.imag, half) * delta_x

    #plt.stem(np.arange(-2, 2 + delta_x, delta_x), gdm_real, markerfmt=' ', linefmt='b-', label='real')
    plt.plot(f, gdm_real * np.exp(1j * 2 * math.pi * f))
    plt.show()
    plt.plot(f, gdm_imag * 1j * np.exp(1j * 2 * math.pi * f))
    plt.show()


def problem_d():
    delta_x = .05
    def gx(x):
        return x * math.exp(-abs(x) ** (3 / 2))
    
def test():
    delta_x = .1
    N = int(2 / delta_x) + 1
    def gx(x):
        return (1 - np.abs((x - 1))) ** 2
    gdn = gx(np.arange(0, 2+delta_x,delta_x))
    gdm = np.fft.fft(gdn)
    gdm_real = np.roll(gdm.real, 10) * delta_x
    gdm_imag = np.roll(gdm.imag, 10) * delta_x
    f = np.arange(-10,11,1) / delta_x / N
    plt.plot(f, gdm_real * np.exp(1j * 2 * math.pi * f))
    plt.plot(f, gdm_imag * 1j * np.exp(1j * 2 * math.pi * f))
    plt.show()

#test()  
problem_a()
# problem_d()