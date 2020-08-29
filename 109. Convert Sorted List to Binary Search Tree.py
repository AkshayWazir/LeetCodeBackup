class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(array):
    def recur(arr):
        if len(arr) == 0:
            return None
        t_node = TreeNode(arr[len(arr) // 2])
        t_node.left = recur(arr[:len(arr) // 2])
        t_node.right = recur(arr[(len(arr) // 2) + 1:])
        return t_node

    return recur(array)


print(make_tree([-10, -3, 0, 5, 9]))
