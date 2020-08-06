class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check(root):
    if root is None:
        return []
    stack = [root]
    res = [[root.val]]
    while len(stack) != 0:
        temp_arr, temp_n = [], 0
        tv = []
        for i in range(len(stack)):
            temp_n = i + 1
            if stack[i] is None:
                continue
            stack += [stack[i].left, stack[i].right]
            if stack[i].left is not None:
                tv.append(stack[i].left.val)
            if stack[i].right is not None:
                tv.append(stack[i].right.val)
        res.append(tv)
        stack = stack[temp_n:]
    return res[-3::-1]


rt = TreeNode(1)
rt.left = TreeNode(2)
rt.right = TreeNode(2)
rt.left.right = TreeNode(4)
rt.right.left = TreeNode(4)
print(check(rt))
