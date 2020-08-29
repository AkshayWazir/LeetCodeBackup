def pascal(r):
    res = []
    for i in range(1, r + 1):
        if i == 1:
            res.append([1])
        elif i == 2:
            res.append([1, 1])
        else:
            temp = [1, 1]
            for j in range(i - 2):
                temp.insert(j + 1, res[-1][j] + res[-1][j + 1])
            res.append(temp)
    return res


print(pascal(5))
