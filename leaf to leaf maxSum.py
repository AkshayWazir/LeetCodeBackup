import math


def get_max(node):
    if node is None:
        return -math.inf
    if node.left is None and node.right is None:
        return node.val
    l_max = get_max(node.left)
    r_max = get_max(node.right)
    if node.left is not None and node.right is not None:
        res = max(max_number, l_max + r_max + node.val)


max_number = -math.inf
