import numpy as np

y = np.array([5, 3, 5, 3, 1, 3, 2, 3])

def problem_a():
    b = []
    for m in range(3):
        b.append(np.arange(8) ** (m / 2))
    b = np.array(b).T
    bt = b.T
    c = np.matmul(np.linalg.inv(np.matmul(bt, b)), np.matmul(bt, y))
    print(np.linalg.norm(y - np.matmul(b, c), 2))
    return c

def problem_d():
    b = []
    for m in range(4):
        b.append(np.arange(8) ** (m / 2))
    b = np.array(b).T
    bt = b.T
    d = np.matmul(np.linalg.inv(np.matmul(bt, b)), np.matmul(bt, y))
    print(np.linalg.norm(y - np.matmul(b, d), 2))
    return d
c = problem_a()
d = problem_d()
print('c =', c)
print('d =', d)