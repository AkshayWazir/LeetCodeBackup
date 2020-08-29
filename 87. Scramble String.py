def scrambled(s1, s2) -> bool:
    def recur(sw1, sw2):
        l1 = sorted(list(sw1))
        l2 = sorted(list(sw2))
        if len(l1) == len(l2) <= 1:
            return True
        elif l1 != l2:
            return False
        else:
            r1 = recur("".join(list(sw1)[:len(l1) // 2]), "".join(list(sw2)[:len(l2) // 2]))
            r2 = recur("".join(list(sw1)[len(l1) // 2:]), "".join(list(sw2)[len(l2) // 2:]))
            return r1 and r2

    if len(s1) == len(s2) == 1:
        return s1 == s2
    else:
        return recur(s1, s2)


def sol(s1, s2):
    n, m = len(s1), len(s2)
    if n != m or sorted(s1) != sorted(s2):
        return False
    if n < 4 or s1 == s2:
        return True
    f = sol
    for i in range(1, n):
        if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
            return True
    return False


test_cases = [
    ["a", "b", False],
    ["abcde", "caebd", True],
    ["greate", "rgtae", True],
    ["", "", True],
    ["abb", "bab", True]

]
for i, j, k in test_cases:
    print(sol(i, j) == k, " values are ", i, "  ", j)
