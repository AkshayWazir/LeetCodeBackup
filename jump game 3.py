def jump_game_memory(array, start):
    path_finder = {}
    for i in range(len(array)):
        temp_array = []
        if i - array[i] >= 0:
            temp_array.append(i - array[i])
        if i + array[i] < len(array):
            temp_array.append(i + array[i])
        path_finder[i] = temp_array
    found = [start]
    remember = [False for i in range(len(array))]
    while len(found) != 0:
        if array[found[0]] != 0:
            remember[found[0]] = True
            for i in path_finder[found[0]]:
                if not remember[i]:
                    found.append(i)
            found.pop(0)
        else:
            return True
    return False


print(jump_game_memory([3, 0, 2, 1, 2], 2))
