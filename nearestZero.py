import math


def search(row, column, dist):
    if row < 0 or column < 0 or row == len(matt) or column == len(matt[row]):
        return math.inf
    elif matt[row][column] == 0:
        return dist
    else:
        if matt[row][column] == -1:
            return math.inf
        else:
            matt[row][column] = -1
            res = search(row - 1, column, dist + 1)
            res1 = search(row, column - 1, dist + 1)
            res2 = search(row + 1, column, dist + 1)
            res3 = search(row, column + 1, dist + 1)
            matt[row][column] = 1
            return min(res, res1, res2, res3)


def search_min_eff(matrix):
    temp_matrix = []
    for i in range(len(matrix)):
        row_temp = []
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                row_temp.append(search(i, j, 0))
            else:
                row_temp.append(0)
        temp_matrix.append(row_temp)
    return temp_matrix


matt = [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 1, 0]]
matt = search_min_eff(matt)
print(matt)
