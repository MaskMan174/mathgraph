from sympy import *
import numpy as np
import dill
import cloudpickle as pk


def func_from_in(s: str):
    x = symbols('x')
    f = sympify(s)
    func = pk.dumps(lambdify(x, f, 'numpy'))
    return f, func


def show_s_by_func(func, a, b, h0=0):
    import matplotlib.pyplot as plt
    func = pk.loads(func)
    x = np.linspace(a, b, 100)
    plt.plot(x, func(x), '-')
    plt.fill_between(x, func(x), h0, color="green")
    plt.grid()

    plt.show()
