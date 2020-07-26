def insert_interval(ins, n_ins):
    for i in range(len(ins)):
        if ins[i][0] <= n_ins[0] <= ins[i][1]:
            n_ins[0] = min(ins[i][0], n_ins[0])
        if ins[i][0] <= n_ins[1] <= ins[i][1]:
            n_ins[1] = max(ins[i][1], n_ins[1])
    res = [n_ins]
    pos = 0
    for i in ins:
        if i[0] < n_ins[0] and i[1] < n_ins[0]:
            res.insert(pos, i)
            pos += 1
        elif i[0] > n_ins[1] and i[1] > n_ins[1]:
            res.insert(pos, i)
            pos += 1
        else:
            pos += 1
    res.sort()
    return res


print(insert_interval([[1, 5]], [0, 0]))
