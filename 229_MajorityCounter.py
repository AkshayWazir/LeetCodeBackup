from collections import Counter


def count(s):
    c = Counter(s)
    res = set(s)
    return [i for i in res if c[i] > len(s) // 3]


print(count([1, 1, 1, 2, 2, 2, 3, 3]))
