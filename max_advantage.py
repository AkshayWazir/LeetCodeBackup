#  brute force solution
def get_max_arr(a, b, temp):
    global choice, temp_max
    if len(temp) == len(b):
        res = sum([1 if temp[i] > b[i] else 0 for i in range(len(b))])
        if res > temp_max:
            choice = [j for j in temp]
            temp_max = res
    for i in range(len(a)):
        temp.append(a.pop(i))
        get_max_arr(a, b, temp)
        a.insert(i, temp.pop())


def optimal_sol(a, b):
    a.sort()
    s = [k for k in b]
    b.sort()
    temp_res = {}
    count = 0
    for i in b:
        for j in range(len(a)):
            if a[j] > i:
                if temp_res.get(i, -1) == -1:
                    temp_res[i] = [a[j]]
                else:
                    temp_res[i].append(a[j])
                count += 1
                a.pop(j)
                break
    res = []
    for i in range(len(s)):
        if temp_res.get(s[i], -1) != -1:
            if len(temp_res[s[i]]) == 0:
                res.append(a.pop(0))
            else:
                res.append(temp_res[s[i]].pop(0))
        else:
            res.append(a.pop(0))
    return res


a, b = [2, 0, 4, 1, 2], [1, 3, 0, 0, 2]
c, d = [3451, 9210, 6762, 6256, 9339, 306, 6025, 1879, 3969, 1818], [3491, 9014, 7254, 8463, 754, 3008, 7842, 404, 1897, 818]
e, f = [28, 47, 45, 8, 2, 10, 25, 35, 43, 37, 33, 30, 33, 20, 33, 42, 43, 36, 34, 3, 16, 23, 15, 10, 19, 42, 13, 47, 0, 21, 36, 38, 0, 5, 3, 28, 4, 20, 14, 5, 19, 22, 29, 17, 3, 16, 35, 0, 26, 0], \
       [44, 10, 27, 4, 27, 40, 46, 40, 45, 0, 41, 2, 44, 50, 36, 30, 37, 4, 44, 4, 12, 13, 35, 20, 19, 25, 38, 42, 43, 14, 2, 4, 5, 38, 4, 38, 0, 35, 12, 32, 38, 33, 3, 1, 19, 46, 23, 13, 24, 41]
print(optimal_sol(a, b))
