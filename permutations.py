master = []


def ret_perm(arr, current):
    if len(arr) == 0:
        master.append(list(map(int, current.split())))
    else:
        for i in range(len(arr)):
            if arr[i] not in arr[:i]:
                temp = arr.pop(i)
                ret_perm(arr, current + " " + str(temp))
                arr.insert(i, temp)


ret_perm([1, 2, 2], "")
print(master)
