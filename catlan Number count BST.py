def fac(n):
    a = 1
    for i in range(n):
        a *= i + 1
    return a


def cat(a):
    return fac(2 * a) // ((fac(a + 1)) * fac(a))

