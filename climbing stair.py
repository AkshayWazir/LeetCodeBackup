def climb(target):
    if target < 2:
        return target
    path = [1, 2]
    for i in range(2, target):
        one_jumps = i - 1
        two_jumps = i - 2
        count = 0
        if one_jumps >= 0:
            count += path[one_jumps]
        if two_jumps >= 0:
            count += path[two_jumps]
        path.append(count)
    return path[len(path) - 1]


for i in range(1, 45):
    print(i, " : ", climb(i))
