class Node:
    def __init__(self, r, c, val):
        self.row = r
        self.col = c
        self.val = val


def count_islands(arr):
    count = 0
    memory = [[False for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if not memory[i][j] and arr[i][j] == "1":
                temp, memory = bfs(i, j, memory, arr)
                count += temp
    return count


def bfs(r, c, mem, temparr):
    temp = [Node(r, c, temparr[r][c])]
    mem[r][c] = True
    while len(temp) != 0:
        if temp[0].val == "1":
            if temp[0].col - 1 >= 0:
                if not mem[temp[0].row][temp[0].col - 1]:
                    temp.append(Node(temp[0].row, temp[0].col - 1, temparr[temp[0].row][temp[0].col - 1]))
                    mem[temp[0].row][temp[0].col - 1] = True

            if temp[0].row - 1 >= 0:
                if not mem[temp[0].row - 1][temp[0].col]:
                    temp.append(Node(temp[0].row - 1, temp[0].col, temparr[temp[0].row - 1][temp[0].col]))
                    mem[temp[0].row - 1][temp[0].col] = True

            if temp[0].col + 1 < len(temparr[0]):
                if not mem[temp[0].row][temp[0].col + 1]:
                    temp.append(Node(temp[0].row, temp[0].col + 1, temparr[temp[0].row][temp[0].col + 1]))
                    mem[temp[0].row][temp[0].col + 1] = True

            if temp[0].row + 1 < len(temparr):
                if not mem[temp[0].row + 1][temp[0].col]:
                    temp.append(Node(temp[0].row + 1, temp[0].col, temparr[temp[0].row + 1][temp[0].col]))
                    mem[temp[0].row + 1][temp[0].col] = True
        temp.pop(0)
    return [1, mem]


print(count_islands([
    ["1", "1", "1", "1", "0"],
    ["1", "0", "0", "1", "0"],
    ["0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "0"]]
))
