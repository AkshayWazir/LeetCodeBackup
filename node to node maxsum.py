import math


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_ms_node(node):
    if node is None:
        return -math.inf
    res_l, res_r = -math.inf, -math.inf
    if node.left is not None:
        res_l = get_ms_node(node.left)
    if node.right is not None:
        res_r = get_ms_node(node.right)


curr_max = -math.inf
node = Node(10)
