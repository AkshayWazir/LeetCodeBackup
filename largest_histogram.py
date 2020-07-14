def find_largest_histogram(array):
    dp = [[0 for i in range(len(array))] for i in range(len(array))]
    for i in range(len(array)):
        dp[i][i] = array[i]
    for i in range(1, len(array)):
        for j in range(len(array) - i):
            temp_min = min(array[j], array[i + j]) * (i + 1)
            if len(array[j + 1:i + j]) != 0 and min(array[j], array[i + j]) > min(array[j + 1:i + j]):
                dp[j][j + i] = max(dp[j][j + i - 1], dp[j + 1][j + i], min(array[j + 1:i + j]) * (i + 1))
            else:
                dp[j][j + i] = max(dp[j][j + i - 1], dp[j + 1][j + i], temp_min)
    return dp[0][len(array) - 1]


def efficient_solution(array):
    max_area = 0
    stack = []
    for i, h in enumerate(array):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))
    for i, h in stack:
        max_area = max(max_area, h * (len(array) - i))
    return max_area


print(find_largest_histogram([2, 1, 5, 6, 2, 3]))
