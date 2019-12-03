# here blocked path are 1 and open are 0
import math


# uses depth first search
def search(r, c, dist):
    if r < 0 or c < 0 or r == len(matrix) or c == len(matrix[r]):
        return math.inf
    elif r == len(matrix) - 1 and c == len(matrix[r]) - 1:
        return dist
    else:
        if matrix[r][c] == 1:
            return math.inf
        else:
            matrix[r][c] = 1
            res = search(r - 1, c, dist + 1)
            res1 = search(r, c - 1, dist + 1)
            res2 = search(r + 1, c, dist + 1)
            res3 = search(r, c + 1, dist + 1)
            matrix[r][c] = 0
            return min(res, res1, res2, res3)


# uses Breath first search
def seach_breath(r, c, dist):
    positions = [[r, c, dist]]
    while len(positions) != 0:
        for i in positions:
            positions.append()


matrix = []
rows, columns = list(map(int, input().split()))
for i in range(rows):
    temp = list(map(int, input().split()))
    matrix.append(temp)
print(search(0, 0, 0))
