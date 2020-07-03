def bfs_paths(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if i + 1 < len(array) and array[i + 1][j] != 1:
                if j + 1 < len(array[0]) and array[i][j + 1] != 1:
                    array[i + 1][j] += array[i][j] + 1
                    array[i][j + 1] += array[i][j] + 1
                else:
                    if j + 1 < len(array[0]):
                        array[i + 1][j] += array[i][j]
            else:
                if j + 1 < len(array[0]) and array[i][j + 1] != 1:
                    array[i][j] += array[i][j]
    return array


res = bfs_paths([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
for k in res:
    print(k)
