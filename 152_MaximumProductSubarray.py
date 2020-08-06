import math


def get_max_product(arr):
    def give_prod(s, e):
        nonlocal arr
        temp = 1
        for i in arr[s:e + 1]:
            temp *= i
        return temp

    dp = [[-math.inf for i in range(len(arr))] for j in range(len(arr))]
    ma = -math.inf
    for i in range(len(arr)):
        dp[i][i] = arr[i]
        if arr[i] > ma:
            ma = max(arr[i], ma)
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            res = give_prod(j, i + j)
            if res > ma:
                ma = res
    return ma


def rec_solution(arr):
    def recur(ar, cons, var):
        if cons == var:
            nonlocal ma
            temp = 1
            for i in ar:
                temp *= i
            ma = max(temp, ma)
        else:
            recur(ar, cons, var + 1)
            recur(ar[:len(ar)], cons, var + 1)
            recur(arr[1:], cons, var + 1)

    ma = -math.inf
    recur(arr, len(arr), 0)
    return ma


def dp_sol(arr):
    class Node:
        def __init__(self, m_max, m_min):
            self.max_val = m_max
            self.min_val = m_min

    dp = [Node(math.inf, -math.inf) for i in range(len(arr))]
    dp[0] = Node(arr[0], arr[0])
    res = dp[0].max_val
    for i in range(1, len(arr)):
        prev = dp[i - 1]
        t_max = max(max(arr[i], arr[i] * prev.max_val), arr[i] * prev.min_val)
        t_min = min(min(arr[i], arr[i] * prev.max_val), arr[i] * prev.min_val)
        dp[i] = Node(t_max, t_min)
        res = max(t_max, res)
    return res


print(dp_sol([2, 3, -2, 4, 3, -4]))
# print(get_max_product([2, 3, -2, 4, 3, -4]))
# print(rec_solution([2, 3, -2, 4, 3, -4]))
