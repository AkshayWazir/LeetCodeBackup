def make_spiral(n):
    matrix = [[-1 for i in range(n)] for j in range(n)]
    directions = [True, False, False, False]
    temp = 1
    x, y = 0, 0
    for i in range(n ** 2):
        matrix[y][x] = temp
        temp += 1
        if directions[0]:
            if x + 1 < n and matrix[y][x + 1] == -1:
                x += 1
            else:
                directions = change_direction(directions)
                y += 1
        elif directions[1]:
            if y + 1 < n and matrix[y + 1][x] == -1:
                y += 1
            else:
                directions = change_direction(directions)
                x -= 1
        elif directions[2]:
            if x - 1 >= 0 and matrix[y][x - 1] == -1:
                x -= 1
            else:
                directions = change_direction(directions)
                y -= 1
        elif directions[3]:
            if y - 1 >= 0 and matrix[y - 1][x] == -1:
                y -= 1
            else:
                directions = change_direction(directions)
                x += 1
    return matrix


def change_direction(array):
    for i in range(len(array)):
        if array[i] and i == 3:
            array[i], array[0] = False, True
            break
        elif array[i]:
            array[i + 1], array[i] = True, False
            break
    return array


print(make_spiral(5))
