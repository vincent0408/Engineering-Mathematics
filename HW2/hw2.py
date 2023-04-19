import numpy as np
import math

b = np.zeros((5, 16))
w1 = np.ones(16)
w2 = np.array([1 / math.sqrt(n + 1) for n in range(16)])

for i in range(5):
    for j in range(16):
        b[i][j] = math.cos(i * j * j)

def GS(w):
    b_copy = np.copy(b)
    for i in range(5):
        c = np.zeros(16)
        for j in range(i):
            c += np.sum(w * b_copy[i] * b_copy[j]) * b_copy[j]
        b_copy[i] -= c
        b_copy[i] = b_copy[i] / np.sqrt(np.sum(w * b_copy[i] * b_copy[i]))
    return b_copy

def checkOrthonormal(c_set, w):
    threshold = 1e-10
    for i in range(5):
        if(np.sqrt(np.sum(w * c_set[i] * c_set[i])) - 1 > threshold):
            return False
    for i in range(5):
        for j in range(i):
            if(np.sum(w * c_set[i] * c_set[j]) > threshold):
                return False
    return True

c1 = GS(w1)
if(checkOrthonormal(c1, w1)):
    print('b_k after Gram-Schnidt without weight:\n', c1)
c2 = GS(w2)
if(checkOrthonormal(c2, w2)):
    print('b_k after Gram-Schnidt with weight:\n', c2)
