class Node:
    def __init__(self, name, distance):
        self.name = name
        self.dist = distance


def dejiktras(arr, start, end):
    visited = [False for i in range(len(arr))]
    stack = [0]
    path = [start]
    while len(stack) != 0:
        times = len(stack)
        for i in range(times):
            for j in :


nodes = [[Node("b", 4), Node("c", 5)],  # a
         [Node("a", 4), Node("d", 3), Node("e", 2)],  # b
         [Node("a", 5), Node("d", 7), Node("f", 2)],  # c
         [Node("b", 3), Node("e", 2), Node("f", 1), Node("c", 7)],  # d
         [Node("b", 2), Node("d", 2), Node("f", 4)],  # e
         [Node("c", 2), Node("d", 1), Node("e", 4)]]  # f
