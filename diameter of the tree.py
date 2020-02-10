class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_m_depth(node):
    if node is None:
        return [0, -1]
    res = get_m_depth(node.left)
    res1 = get_m_depth(node.right)
    return [max(max(res[0], res1[0]), res[1] + res1[1] + 2), max(res[1], res[1]) + 1]


a = Node(10)
a.left = Node(20)
a.right = Node(70)
a.left.left = Node(30)
a.left.right = Node(40)
a.left.right.left = Node(50)
a.left.right.right = Node(60)
print(get_m_depth(a)[0])
