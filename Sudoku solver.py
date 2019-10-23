# function to display
def display_the_matrix(disp):
    for i in range(len(disp)):
        for j in range(len(disp[0])):
            print(disp[i][j], end=" ")
        print()


# horizontal check
def h_c(row, num):
    if num in sudoku[row]:
        return True
    else:
        return False


# Vertical Check
def v_c(col, num):
    if num in [sudoku[j][col] for j in range(9)]:
        return True
    else:
        return False


# Box check
def b_c(row, col, num):
    s_r = (row // 3) * 3
    s_c = (col // 3) * 3
    temp = []
    for tr in range(s_r, s_r + 3):
        for tc in range(s_c, s_c + 3):
            temp.append(sudoku[tr][tc])
    if num in temp:
        return True
    else:
        return False


# Now we will check and feed the empty Sudoku matrix
def fill_the_matrix(matrix, r, c):
    if c == 9:
        fill_the_matrix(matrix, r + 1, 0)
    elif r == 9:
        display_the_matrix(matrix)
    elif matrix[r][c] != 0:
        fill_the_matrix(matrix, r, c + 1)
    else:
        for i in range(1, 10):
            if not h_c(r, i) and not v_c(c, i) and not b_c(r, c, i):
                matrix[r][c] = i
                fill_the_matrix(matrix, r, c + 1)
                matrix[r][c] = 0


# first we take the 2d array
sudoku = []
for i in range(9):
    arr = list(input())
    arr = [0 if arr[i] == "-" else int(arr[i]) for i in range(9)]
    sudoku.append(arr)

fill_the_matrix(sudoku, 0, 0)
