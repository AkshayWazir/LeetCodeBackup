import math


def dp_solution(array):
    dp = [[-math.inf for i in range(len(array))] for j in range(len(array))]
    for i in range(len(array) - 1):
        dp[i][i + 1] = array[i + 1] - array[i]
    for i in range(2, len(array)):
        for j in range(len(array) - i):
            hn = dp[j][j + i - 1]
            vn = dp[j + 1][j + i]
            cu = array[j + i] - array[j]
            dp[j][i + j] = max(hn, vn, cu)
    return dp[0][len(array) - 1]


def two_var_solution(array):
    min_num, max_profit = math.inf, 0
    for i in range(len(array)):
        if array[i] < min_num:
            min_num = array[i]
        elif array[i] - min_num > max_profit:
            max_profit = array[i] - min_num
    return max_profit


print(dp_solution([7, 1, 5, 3, 6, 4]))
