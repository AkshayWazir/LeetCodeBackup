def gray_code(n: int):
    res = [0]
    for i in range(n):
        for j in range(len(res) - 1, -1, -1):
            s = res[j] | 1 << i
            print('{0:03b}'.format(s))
            res.append(s)
    return res


gray_code(3)
