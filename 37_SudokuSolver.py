def solve(sudoku, cur_r, cur_c):
    global final
    if cur_r == cur_c == 8:
        final = [[s for s in j] for j in sudoku]
    if cur_c >= 9 or cur_r >= 9:
        if cur_r == 9 and cur_c < 8:
            solve(sudoku, 0, cur_c + 1)
        return
    elif sudoku[cur_r][cur_c] != ".":
        solve(sudoku, cur_r + 1, cur_c)
        return
    else:
        poss = [str(i + 1) for i in range(9)]
        v_pre = [sudoku[j][cur_c] for j in range(9) if sudoku[j][cur_c] != "."]
        grid = [[], [], []]
        for i in range(3 * (cur_r // 3), 3 * (cur_r // 3) + 3):
            for j in range(3 * (cur_c // 3), 3 * (cur_c // 3) + 3):
                grid[cur_r // 3].append(sudoku[i][j]) if sudoku[i][j] != "." else None
        g_pre = grid[0] + grid[1] + grid[2]
        i = 0
        while i < len(poss):
            if poss[i] in sudoku[cur_r] or poss[i] in v_pre or poss[i] in g_pre:
                poss.pop(i)
            else:
                i += 1
        for var in poss:
            sudoku[cur_r][cur_c] = var
            solve(sudoku, cur_r + 1, cur_c)
            sudoku[cur_r][cur_c] = "."


maze = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
final = []
solve(maze, 0, 0)
for i in final:
    print(i)
