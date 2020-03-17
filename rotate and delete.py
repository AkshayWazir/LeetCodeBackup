def rad(array):
    delet_pos = 0
    direction = -1
    temp = len(array) - 2
    while temp != 0:
        array.insert(0, array[-1])
        array.pop(len(array) - 1)
        if direction < 0:
            if len(array) - 1 - delet_pos < 0:
                direction, delet_pos = 1, 1
                array.pop(0)
            else:
                array.pop(len(array) - 1 - delet_pos)
        else:
            if delet_pos >= len(array):
                direction, delet_pos = -1, 1
                array.pop(len(array) - 1 - delet_pos)
            else:
                array.pop(delet_pos)
        delet_pos += 1
        temp -= 1
    return array[-1]


def rad2(array):
    pos = -1
    while len(array) > 1:
        array.insert(0, array[-1])
        array.pop(len(array) - 1)
        try:
            array.pop(pos)
        except IndexError:
            array.pop(0)
        pos -= 1
    print(array[0])


testCases = int(input())
for i in range(testCases):
    n = int(input())
    arr = list(map(int, input().split()))
    rad2(arr)
