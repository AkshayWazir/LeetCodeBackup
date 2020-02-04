class Node:
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.direction = [1, 0, 0, 0]  # r d l u

    def change_direction(self):
        if self.direction[0] == 1:
            self.direction[0], self.direction[1] = 0, 1
        elif self.direction[1] == 1:
            self.direction[1], self.direction[2] = 0, 1
        elif self.direction[2] == 1:
            self.direction[2], self.direction[3] = 0, 1
        elif self.direction[3] == 1:
            self.direction[3], self.direction[0] = 0, 1


def spiral(matrix):
    memory = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
    result = []
    snake = Node(0, 0)
    max_rows, max_columns = len(matrix), len(matrix[0])
    while True:
        if len(result) == (max_rows * max_columns) - 1:
            result.append(matrix[snake.row][snake.column])
            break
        if snake.direction[0] == 1:
            if snake.column + 1 == max_columns:
                snake.change_direction()
            elif memory[snake.row][snake.column + 1]:
                snake.change_direction()
            else:
                memory[snake.row][snake.column] = True
                result.append(matrix[snake.row][snake.column])
                snake.column += 1
        elif snake.direction[1] == 1:
            if snake.row + 1 == max_rows:
                snake.change_direction()
            elif memory[snake.row + 1][snake.column]:
                snake.change_direction()
            else:
                memory[snake.row][snake.column] = True
                result.append(matrix[snake.row][snake.column])
                snake.row += 1
        elif snake.direction[2] == 1:
            if snake.column - 1 == -1:
                snake.change_direction()
            elif memory[snake.row][snake.column - 1]:
                snake.change_direction()
            else:
                memory[snake.row][snake.column] = True
                result.append(matrix[snake.row][snake.column])
                snake.column -= 1
        elif snake.direction[3] == 1:

            if memory[snake.row - 1][snake.column]:
                snake.change_direction()
            else:
                memory[snake.row][snake.column] = True
                result.append(matrix[snake.row][snake.column])
                snake.row -= 1
    return result


print(spiral([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]))
