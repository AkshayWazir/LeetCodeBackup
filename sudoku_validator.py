def h_c(row, column, num):
    temp = ["." if i == column else sudoku[row][i] for i in range(9)]
    if num in temp:
        return True
    else:
        return False


# Vertical Check
def v_c(row, col, num):
    temp = [sudoku[s][col] for s in range(9)]
    temp.pop(row)
    if num in temp:
        return True
    else:
        return False


# Box check
def b_c(row, col, num):
    s_r = (row // 3) * 3
    s_c = (col // 3) * 3
    for tr in range(s_r, s_r + 3):
        for tc in range(s_c, s_c + 3):
            if num == sudoku[tr][tc] and tc != col and tr != row:
                return True
    return False


def validate():
    for i in range(9):
        for j in range(9):
            temp = sudoku[i][j]
            if sudoku[i][j] == ".":
                pass
            else:
                if h_c(i, j, temp) or v_c(i, j, temp) or b_c(i, j, temp):
                    print(i, " ", j)
                    return False
    return True


sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(validate())
