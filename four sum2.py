def four_sum_count(a, b, c, d):
    count = 0
    memory = dict()
    for i in a:
        for j in b:
            temp = i + j
            if memory.get(temp, -1) != -1:
                memory[temp] += 1
            else:
                memory[temp] = 1
    for i in c:
        for j in d:
            temp = -(i + j)
            if memory.get(temp, -1) != -1:
                count += memory.get(temp)
    return count


