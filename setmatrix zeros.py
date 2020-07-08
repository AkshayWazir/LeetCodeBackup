def get_matrix(array):
    zeros = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 0:
                zeros.append([i, j])
    for i in zeros:
        array[i[0]] = [0 for j in range(len(array[0]))]
        for j in range(len(array)):
            array[j][i[1]] = 0
    return array


test1 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

test1 = get_matrix(test1)
for i in test1:
    print(i)
