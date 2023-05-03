import math
def problem_a():
    delta_x = .02
    def gx(x):
        return math.sin(math.pi * x ** 3 / 8)
    


def problem_d():
    delta_x = .05
    def gx(x):
        return x * math.exp(-abs(x) ** (3 / 2))
    
problem_a()
# problem_d()