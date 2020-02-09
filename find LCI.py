# here LCA stands for Least common Ancestor
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def give_node(node, target):
    if node is None:
        return [False, -1]
    stat, stat1 = False, False
    val1, val = -1, -1
    if node.left is not None:
        stat, val = give_node(node.left, target)
    if node.right is not None:
        stat1, val1 = give_node(node.right, target)
    if stat1 and stat:
        return [True, node.val]
    elif stat1:
        if node.val in target:
            return [True, node.val]
        return [stat1, val1]
    elif stat:
        if node.val in target:
            return [True, node.val]
        return [stat, val]
    else:
        if node.val in target:
            return [True, 1]
        else:
            return [False, -1]


a = Node(10)
a.left = Node(20)
a.right = Node(70)
a.left.left = Node(30)
a.left.right = Node(40)
a.left.right.left = Node(50)
a.left.right.right = Node(60)
print(give_node(a, [40, 60]))
