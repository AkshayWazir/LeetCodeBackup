from math import factorial


# inspiration
def get_permutation(n, k):
    k -= 1
    ans, digits = [], list(range(1, n + 1))
    for i in range(n):
        d, k = divmod(k, factorial(n - i - 1))
        ans.append(digits.pop(d))
    return "".join(str(x) for x in ans)


def get_permut(n, k):
    k -= 1
    solution, current = [], [i + 1 for i in range(n)]
    for i in range(n):
        dividend, k = divmod(k, factorial(n - i - 1))
        solution.append(current.pop(dividend))
    return "".join([str(solution[i]) for i in range(n)])


print(get_permut(4, 9))
print(get_permutation(4, 9))
