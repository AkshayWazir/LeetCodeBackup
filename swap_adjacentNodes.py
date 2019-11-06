class Node:
    def __init__(self, num):
        self.val = num
        self.next = None


def add_to_chain(node, value):
    node.next = Node(value)
    return node.next


def display(node):
    while node is not None:
        print(node.val, end=" ->")
        node = node.next


def rearrange(ptr):
    papaNode = ptr
    while ptr is not None:
        if ptr.next is not None:
            ptr.val, ptr.next.val = ptr.next.val, ptr.val
            ptr = ptr.next.next
        else:
            return papaNode
    return papaNode


start = Node(None)
iter_ptr = start
n = int(input("Enter the number of nodes :"))
for i in range(n):
    val = int(input("->"))
    iter_ptr = add_to_chain(iter_ptr, val)
display(start.next)
start.next = rearrange(start.next)
print()
display(start.next)
