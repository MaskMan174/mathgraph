from sympy import *
import numpy as np
from math import *


def func_from_in(s: str):
    x = symbols('x')
    f = sympify(s)
    print(f)
    func = lambdify(x, f)
    print(func)
    return f, func


def show_s_by_func(func, a, b, h0=0):
    import matplotlib.pyplot as plt

    x = np.linspace(a, b, 100)
    plt.plot(x, func(x), '-')
    plt.fill_between(x, func(x), h0, color="green")
    plt.grid()

    plt.savefig('saved_figure.png')
    # plt.show()
