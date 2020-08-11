def get_nth(n):
    if n <= 0:
        return False
    elif n == 1:
        return 1
    else:
        t2 = t3 = t5 = 0
        k = list()
        k.append(1)
        for i in range(1, n):
            k.append(min(k[t2] * 2, k[t3] * 3, k[t5] * 5))
            if k[i] == k[t2] * 2:
                t2 += 1
            if k[i] == k[t3] * 3:
                t3 += 1
            if k[i] == k[t5] * 5:
                t5 += 1
        return k[-1]


print(get_nth(10))
