import math


def jumpiJump(arr, current, jumps, currMin):
    if current == len(arr) - 1:
        return min(jumps, currMin)
    elif current >= len(arr) - 1:
        return math.inf
    else:
        for i in range(1, arr[current] + 1):
            tRes = jumpiJump(arr, current + i, jumps + 1, currMin)
            currMin = min(tRes, currMin)
    return currMin


print(jumpiJump([2, 3, 1, 1, 4], 0, 0, math.inf))
