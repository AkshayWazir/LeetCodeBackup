class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check(root):
    level = 1
    stack = [root]
    while len(stack) != 0:
        temp_arr, temp_n = [], 0
        for i in range(len(stack)):
            temp_n = i + 1
            if stack[i] is None:
                continue
            stack += [stack[i].left, stack[i].right]
        stack = stack[temp_n:]
        level += 1
    return level - 2


rt = TreeNode(1)
rt.left = TreeNode(2)
rt.right = TreeNode(2)
rt.left.right = TreeNode(4)
rt.right.left = TreeNode(4)
print(check(rt))
