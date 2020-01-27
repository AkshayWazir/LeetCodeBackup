import copy


class Node:
    def __init__(self, r, c):
        self.row = r
        self.column = c


def counting(grid):
    memory = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    flag = 1
    frames = -1
    while flag == 1:
        flag = 0
        temp = copy.deepcopy(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2 and not memory[i][j]:
                    memory[i][j] = True
                    flag = 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            temp[i - 1][j] = 2
                    if j - 1 >= 0:
                        if grid[i][j - 1] == 1:
                            temp[i][j - 1] = 2
                    if i + 1 < len(grid):
                        if grid[i + 1][j] == 1:
                            temp[i + 1][j] = 2
                    if j + 1 < len(grid):
                        if grid[i][j + 1] == 1:
                            temp[i][j + 1] = 2
        grid = copy.deepcopy(temp)
        frames += 1
    if grid == [[0]]:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 1:
                return -1
    return frames - 1



print(counting([
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1]
]))
print(counting([[0, 1], [2, 0]]))
