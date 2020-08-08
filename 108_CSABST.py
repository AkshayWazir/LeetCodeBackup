class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate(arr):
    if len(arr) == 0:
        return None
    else:
        node = TreeNode(arr[len(arr) // 2])
        node.left = generate(arr[:len(arr) // 2])
        node.right = generate(arr[(len(arr) // 2) + 1:])
        return node


t1 = [-10, -3, 0, 5, 9]
root = generate(t1)
print(root)
