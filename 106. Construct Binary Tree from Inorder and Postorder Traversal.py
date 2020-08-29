class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(inorder, postorder):
    if not inorder or not postorder:
        return None

    root = TreeNode(postorder.pop())
    inorderIndex = inorder.index(root.val)

    root.right = build_tree(inorder[inorderIndex + 1:], postorder)
    root.left = build_tree(inorder[:inorderIndex], postorder)

    return root


res = build_tree([1, 2, 3], [3, 2, 1])
print(res)
