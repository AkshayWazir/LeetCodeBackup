class Node:
    def __init__(self, row, col, su):
        self.r = row
        self.c = col
        self.sum = su


def bfs_mps(array):
    if len(array) == 1:
        return sum(array[0])
    elif len(array[0]) == 1:
        temp = 0
        for i in array:
            temp += i[0]
        return temp
    try:
        res = [Node(1, 0, array[0][0] + array[1][0]), Node(0, 1, array[0][0] + array[0][1])]
    except IndexError:
        if len(array) < 2 and len(array[0]) < 2:
            return array[0][0]
        elif len(array) < 2:
            return array[0][0] + array[0][1]
        else:
            return array[0][0] + array[1][0]
    for i in range(len(array) + len(array[0]) - 3):
        tl = len(res)
        for j in range(tl):
            try:
                res.append(Node(res[0].r, res[0].c + 1, res[0].sum + array[res[0].r][res[0].c + 1]))
                res.append(Node(res[0].r + 1, res[0].c, res[0].sum + array[res[0].r + 1][res[0].c]))
                res.pop(0)
            except IndexError:
                if res[0].c + 1 == len(array[0]) and res[0].r + 1 < len(array):
                    res.append(Node(res[0].r + 1, res[0].c, res[0].sum + array[res[0].r + 1][res[0].c]))
                res.pop(0)
        temp_state = [i.sum for i in res]
    return min(temp_state)


def dp_mps(array):
    lr = len(array)
    if lr == 1:
        return sum(array[0])
    lc = len(array[0])
    if lc == 1:
        return sum([array[i][0] for i in range(lr)])
    if lr == 0 and lc == 0:
        return 0
    dp = [[0 for j in range(lc)] for j in range(lr)]
    dp[0][0] = array[0][0]
    for i in range(1, lr):
        dp[i][0] = dp[i - 1][0] + array[i][0]
    for i in range(1, lc):
        dp[0][i] = dp[0][i - 1] + array[0][i]

    for i in range(1, lr):
        for j in range(1, lc):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + array[i][j]

    return dp[lr - 1][lc - 1]


print(dp_mps([
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]))

print(dp_mps([
    [7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5],
    [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
    [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8],
    [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
    [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4],
    [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
    [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4],
    [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
    [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3],
    [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
    [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7],
    [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9]
]))
