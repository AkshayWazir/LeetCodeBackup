class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check(root):
    stack = [root]
    while len(stack) != 0:
        temp_arr, temp_n = [], 0
        for i in range(len(stack)):
            temp_n = i + 1
            if stack[i] is None:
                continue
            stack += [stack[i].left, stack[i].right]
            temp_arr += [
                stack[i].left.val if stack[i].left is not None else None,
                stack[i].right.val if stack[i].right is not None else None
            ]
        fh = temp_arr[:temp_n]
        sh = temp_arr[-1:-temp_n - 1:-1]
        if fh != sh:
            return False
        stack = stack[temp_n:]
    return True


rt = TreeNode(1)
rt.left = TreeNode(2)
rt.right = TreeNode(2)
rt.left.right = TreeNode(4)
rt.right.left = TreeNode(4)
print(check(rt))
