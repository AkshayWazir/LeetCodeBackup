def lexcological(arr):
    eleAtX = 0
    eleatx = 0
    for i in range(-2, len(arr) * -1, -1):
        if arr[i] < arr[i + 1]:
            eleAtX = i
            break
    for j in range(-1, len(arr) * -1, -1):
        if arr[j] > arr[eleAtX]:
            eleatx = j
            break
    temp = arr[eleAtX]
    arr[eleAtX] = arr[eleatx]
    arr[eleatx] = temp
    temp = arr[eleAtX + 1:]
    temp.reverse()
    for j in range(0, len(temp)):
        arr[eleAtX + 1 + j] = temp[j]
    return arr
