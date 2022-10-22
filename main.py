from monte_carlo import *
from func_from_input import *


def main():
    s = str(input('Введите функцию: '))
    a, b = map(int, input('Введите промежуток(начало и конец через пробел): ').split())
    iterations = 10000000

    funcs = func_from_in(s)
    f, func = funcs[0], funcs[1]
    scope_of_values = gr_and_leas(func, extr(f), a, b)
    greatest, least = scope_of_values[0], scope_of_values[1]

    print(s_monte_carlo(func, a, b, greatest, least, iterations))
    show_s_by_func(func, a, b, 0)


if __name__ == "__main__":
    main()
