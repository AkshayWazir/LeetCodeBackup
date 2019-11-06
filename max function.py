import math


def ret_max(arr):
    max_1, max_2, max_3, max_4 = -math.inf, -math.inf, -math.inf, -math.inf
    min_1, min_2, min_3, min_4, res = math.inf, math.inf, math.inf, math.inf, -math.inf
    for i in range(len(arr)):
        max_1, max_2 = max(max_1, arr[i] + i), max(max_2, arr[i] - i)
        max_3, max_4 = max(max_3, -arr[i] + i), max(max_4, -arr[i] - i)

        min_1, min_2 = min(min_1, arr[i] + i), min(min_2, arr[i] - i)
        min_3, min_4 = min(min_3, -arr[i] + i), min(min_4, -arr[i] - i)
    res = max(res, max_1 - min_1)
    res = max(res, max_2 - min_2)
    res = max(res, max_3 - min_3)
    res = max(res, max_4 - min_4)
    return res


ar = list(map(int, input().split()))
print(ret_max(ar))
