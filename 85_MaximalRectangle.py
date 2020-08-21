def max_area(height):
    # height [6, 2, 5, 4, 5, 4,5,0]
    # stack  [-1,6]
    # ans    0
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans


def dp_max_finder(heights):
    if not heights:
        return 0
    lessFromLeft = [0] * len(heights)
    lessFromRight = [0] * len(heights)
    lessFromRight[-1] = len(heights)
    lessFromLeft[0] = -1
    for i in range(1, len(heights)):
        p = i - 1
        while p >= 0 and heights[p] >= heights[i]:
            p = lessFromLeft[p]
        lessFromLeft[i] = p
    for i in range(len(heights) - 1, -1, -1):
        p = i + 1
        while p < len(heights) and heights[p] >= heights[i]:
            p = lessFromRight[p]
        lessFromRight[i] = p
    max_a = 0
    for i in range(len(heights)):
        max_a = max(max_a, heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1))
    return max_a


def max_rectangle(matrix):
    if not matrix:
        return 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            matrix[j][i] = matrix[j - 1][i] + matrix[j][i] if j > 0 and matrix[j][i] != 0 else matrix[j][i]
    max_arr = 0
    for k in matrix:
        max_arr = max(dp_max_finder(k), max_arr)
    print(max_arr)


temp = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
max_rectangle(temp)
