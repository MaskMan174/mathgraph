from sympy import *
from math import *


def extr(f):
    x = symbols('x')
    df = diff(f)
    sol = solveset(Eq(df, 0), x)
    return sol


def sort(array):
    less, equal, greater = [], [], []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return array


def gr_and_leas(func, sol, a, b):
    arr = [0, func(a), func(b)]
    for i in sol:
        if (a <= i) and (b >= i):
            arr.append(func(i))
    sort(arr)
    return arr[0], arr[len(arr)-1]


def s_monte_carlo(func, a, b, h, h0, iterations):
    from random import random
    in_p = 0
    for i in range(iterations):
        x, y = random() * abs(a - b) + a, random() * (h - h0) + h0
        if (func(x) < y and (y < 0)) or (func(x) > y and (y > 0)):
            in_p += 1
    result = abs((b - a) * (h - h0) * (in_p / iterations))
    return result
