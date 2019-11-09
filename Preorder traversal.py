class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def set_left(self, val):
        self.left = TreeNode(val)

    def set_right(self, val):
        self.right = TreeNode(val)


def mbt(arr):


tree = [1, 2, 3, None, 4, 5, None]
rem = [False for i in range(len(tree))]
