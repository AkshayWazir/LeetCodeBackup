def sort_colors(array):
    pointers = [-1, -1, -1]
    for i in range(len(array)):
        if array[i] == 0:
            pointers[0] += 1
            pointers[1] += 0 if pointers[1] == -1 else 1
            pointers[2] += 0 if pointers[2] == -1 else 1
            array.insert(pointers[0], array.pop(i))
        elif array[i] == 1:
            pointers[1] = max(pointers[:2]) + 1
            pointers[2] += 0 if pointers[2] == -1 else 1
            array.insert(pointers[1], array.pop(i))
        else:
            pointers[2] = max(pointers[:3]) + 1
            array.insert(pointers[2], array.pop(i))
        print(array)


sort_colors([2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0])
