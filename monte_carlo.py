from numpy.random import random
from sympy import *
import numpy as np
import dill
import cloudpickle as pk


def extr(f, a, b):
    x = symbols('x')
    df = diff(f)
    sol = Intersection(solveset(Eq(df, 0), x, domain=S.Reals), Interval(a, b))
    return sol


def gr_and_leas(f, sol, a, b):
    x = symbols('x')
    arr = [0, f.evalf(subs={x: a}), f.evalf(subs={x: b})]
    for i in sol:
        arr.append(f.evalf(subs={x: i}))
    arr.sort()
    return arr[0], arr[len(arr) - 1]


'''def s_monte_carlo(func, a, b, h, h0, iterations):
    from random import random
    count = 0
    for i in range(iterations):
        x, y = random() * (b - a) + a, random() * (h - h0) + h0
        if (func(x) < y and (y < 0)) or (func(x) > y and (y > 0)):
            count += 1
    return count'''


def stripped_s_monte_carlo(func, a, b, h, h0):
    count = 0
    func = pk.loads(func)
    x, y = random() * (b - a) + a, random() * (h - h0) + h0
    if (func(x) < y and (y < 0)) or (func(x) > y and (y > 0)):
        count += 1
    return count
