import os

from monte_carlo import *
from func_from_input import *
from multiprocessing import Pool
from math import ceil


def main():
    s = str(input('Введите функцию: '))
    a, b = map(int, input('Введите промежуток(начало и конец через пробел): ').split())
    iterations = 1000000
    cores = os.cpu_count()
    funcs = func_from_in(s)
    f, func = funcs[0], funcs[1]
    scope_of_values = gr_and_leas(f, extr(f, a, b), a, b)
    greatest, least = scope_of_values[0], scope_of_values[1]
    args = [(func, a, b, greatest, least) for _ in range(iterations)]

    with Pool(cores) as p:
        res = p.starmap(stripped_s_monte_carlo, args, chunksize=ceil(iterations/cores))
    count = sum(res)
    result = abs((b - a) * (greatest - least) * (float(count) / iterations))

    print(result)
    show_s_by_func(func, a, b, 0)


if __name__ == "__main__":
    main()
