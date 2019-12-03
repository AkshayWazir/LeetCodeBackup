import math


class Stack:
    def __init__(self):
        self.container = []

    def peek(self):
        if len(self.container) != 0:
            return self.container[len(self.container) - 1]

    def pop(self):
        self.container.pop()

    def push(self, obj):
        self.container.append(obj)

    def isEmpty(self):
        return len(self.container) == 0


def patter(arr):
    stack = Stack()
    maximum = -math.inf
    for i in range(len(arr) - 1, -1, -1):
        while not stack.isEmpty() and stack.peek() < arr[i]:
            maximum = stack.peek()
            stack.pop()
        if arr[i] > maximum:
            stack.push(arr[i])
        if arr[i] < maximum:
            return True
    return False


print(patter([1, 2]))
