def find_connected(board):
    def recur(row, column):
        nonlocal mem
        if row < 0 or column < 0 or row >= len(board) or column >= len(board[0]) or mem[row][column] or board[row][column] != "O":
            return False
        else:
            mem[row][column] = True
            recur(row + 1, column)
            recur(row, column + 1)
            recur(row - 1, column)
            recur(row, column - 1)

    if len(board) == 0:
        return
    corners = set()
    mem = [[False for i in range(len(board[0]))] for j in range(len(board))]
    for i in range(len(board)):
        if board[i][0] == "O":
            corners.add((i, 0))
        if board[i][-1] == "O":
            corners.add((i, len(board[i]) - 1))
    for i in range(len(board[0])):
        if board[0][i] == "O":
            corners.add((0, i))
        if board[-1][i] == "O":
            corners.add((len(board) - 1, i))
    for r, c in corners:
        recur(r, c)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "O" and not mem[i][j]:
                board[i][j] = "X"


test_case = [
    ["X", "X", "X", "X", "X", "X", "X"],
    ["X", "O", "O", "X", "X", "X", "X"],
    ["X", "X", "X", "O", "X", "X", "X"],
    ["X", "X", "X", "O", "O", "X", "X"],
    ["X", "X", "O", "X", "O", "X", "O"],
    ["X", "X", "X", "X", "O", "X", "X"],
    ["X", "X", "X", "X", "O", "X", "O"]
]
find_connected(test_case)
for k in test_case:
    print(k)
