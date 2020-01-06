master = []


def para_gen(arr, current):
    if len(arr) == 0:
        count = 0
        for i in current:
            if count < 0:
                return
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
        if count == 0:
            master.append(current)
    else:
        for i in range(len(arr)):
            if arr[i] not in arr[:i]:
                temp = arr.pop(i)
                para_gen(arr, current + temp)
                arr.insert(i, temp)


para_gen(list("((()))"), "")
print(master)
