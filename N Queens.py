class Node:
    def __init__(self, r, c):
        self.row = r
        self.column = c


def count_n_queens(n):
    arrOfQueens = [Node(i, i) for i in range(n)]
