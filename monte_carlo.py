from sympy import *


def extr(f):
    x = symbols('x')
    df = diff(f)
    sol = solveset(Eq(df, 0), x)
    return sol


def gr_and_leas(func, sol, a, b):
    arr = [0, func(a), func(b)]
    for i in sol:
        if (a <= i) and (b >= i):
            arr.append(func(i))
    arr.sort()
    return arr[0], arr[len(arr)-1]


def s_monte_carlo(func, a, b, h, h0, iterations):
    from random import random
    in_p = 0
    for i in range(iterations):
        x, y = random() * (b - a) + a, random() * (h - h0) + h0
        if (func(x) < y and (y < 0)) or (func(x) > y and (y > 0)):
            in_p += 1
    result = abs((b - a) * (h - h0) * (in_p / iterations))
    return result
