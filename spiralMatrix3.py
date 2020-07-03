def start_spiral(r, c, r0, c0):
    directions, path, matrix = [True, False, False, False], [[r0, c0]], [[-1 for i in range(c)] for j in range(r)]
    matrix[r0][c0] = 1
    c0 += 1
    temp = 2
    while check(matrix):
        if 0 <= r0 < r and 0 <= c0 < c:
            path.append([r0, c0])
            matrix[r0][c0] = temp
            temp += 1
        if directions[0]:
            try:
                if matrix[r0 + 1][c0] == -1:
                    directions = change_direction(directions)
                    r0 += 1
                else:
                    c0 += 1
            except:
                directions = change_direction(directions)
                r0 += 1
        elif directions[1]:
            try:
                if matrix[r0][c0 - 1] == -1:
                    directions = change_direction(directions)
                    c0 -= 1
                else:
                    r0 += 1
            except:
                directions = change_direction(directions)
                c0 -= 1
        elif directions[2]:
            try:
                if matrix[r0 - 1][c0] == -1:
                    directions = change_direction(directions)
                    r0 -= 1
                else:
                    c0 -= 1
            except:
                directions = change_direction(directions)
                r0 -= 1
        elif directions[3]:
            try:
                if matrix[r0][c0 + 1] == -1:
                    directions = change_direction(directions)
                    c0 += 1
                else:
                    r0 -= 1
            except:
                directions = change_direction(directions)
                c0 += 1
    return path


def check(matt):
    for i in matt:
        if -1 in i:
            return True
    return False


def change_direction(array):
    for i in range(len(array)):
        if array[i] and i == 3:
            array[i], array[0] = False, True
            break
        elif array[i]:
            array[i + 1], array[i] = True, False
            break
    return array


print(start_spiral(1, 4, 0, 0))
