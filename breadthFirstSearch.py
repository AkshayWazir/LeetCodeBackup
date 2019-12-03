import math
import queue


def bfs(matrix):
    row, column = len(matrix), len(matrix[0])
    que = queue.Queue()
    for i, r in enumerate(matrix):
        for j, ele in enumerate(r):
            if ele == 0:
                que.put(i * column + j)
            elif ele == 1:
                matrix[i][j] = math.inf
    dir = [0, 1, 0, -1, 0]
    while not que.empty():
        top = que.get()
        for k in range(len(dir)-1):
            x = top // column + dir[k]
            y = top % column + dir[k + 1]
            if 0 <= x < row and 0 <= y < column and matrix[x][y] > 0 and matrix[x][y] > matrix[top // column][top % column]:
                matrix[x][y] = matrix[top // column][top % column] + 1
                que.put(x * column + y)
    return matrix


matt = [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 0]]

mat1 = [[0, 1, 1, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 0]]
res = bfs(matt)
for j in res:
    print(j)