import math


def count_path(m, n):
    f = math.factorial
    return f(m + n - 2) / (f(m - 1) * f(n - 1))
