from itertools import permutations
from math import inf


def most_visited(n, rounds):
    start, end = rounds[0], rounds[-1]
    if start > end:
        res = []
        k = start
        while k != end:
            res.append(k)
            if k + 1 > n:
                k = 1
            else:
                k += 1
        res.append(k)
        return sorted(res)
    return [i for i in range(start, end + 1)]


def pile_chooser(piles):
    res = permutations(piles)
    max_ = -inf
    for

print(pile_chooser([9, 8, 7, 6, 5, 1, 2, 3, 4]))
