def shortest_path(triangle):
    res = [triangle[0][0]]
    for i in range(1, len(triangle)):
        temp = []
        for j in range(len(triangle[i]) - 1):
            var = res.pop(0)
            if len(temp) != 0:
                temp[len(temp) - 1] = min(temp[len(temp) - 1], triangle[i][j] + var)
            else:
                temp.append(triangle[i][j] + var)
            temp += [triangle[i][j + 1] + var]
        res += temp
    return min(res)


print(shortest_path([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3],
    [3, 2, 1, 4, 6],
    [4, 5, 7, 8, 1, 9]
]))
