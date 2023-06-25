import numpy as np

entropy = 0

def px(n):
    return np.tanh(1/4) * np.exp(-np.abs(n) / 2)
    
for n in np.arange(-30, 31):
    pxn = px(n)
    entropy += -pxn * np.log(pxn)

print('(a) entropy =', entropy)

def py(n):
    return (31 - np.abs(n)) / 961

kl = 0

for n in np.arange(-30, 31):
    pxn = px(n)
    pyn = py(n)
    kl += pxn * np.log(pxn / pyn)

print('(b) KL divergence =', kl)
