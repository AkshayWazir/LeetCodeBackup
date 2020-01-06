class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_the_tree(arr):
    root = Tree(arr[0])
    stack = [root]
    num = 0
    for i in range(1, len(arr)):
        val1 = arr[i]
        if val1 is not None:
            if num % 2 == 0:
                stack[0].left = Tree(val1)
                stack.append(stack[0].left)
            else:
                stack[0].right = Tree(val1)
                stack.append(stack[0].right)
        if num % 2 != 0:
            stack.pop(0)
        num += 1

    return root


def iterate_in_order(node, re1s):
    if node is None:
        return re1s
    else:
        res1 = iterate_in_order(node.left, re1s)
        return iterate_in_order(node.right, res1 + node.val)


def check_if_bst(node, cur_max, cur_min):
    if not node:
        return True
    if node.val >= cur_max or node.val <= cur_min:
        return False
    left_valid = check_if_bst(node.left, node.val, cur_min)
    right_valid = check_if_bst(node.right, cur_max, node.val)
    return left_valid and right_valid


# res = get_the_tree([5, 4, 6, 1, 4.5, 5.5, 7])
re2 = get_the_tree(["+", "3", "*", None, None, "+", "2", "5", "9"])
# print(check_if_bst(res.right, math.inf, res.val) and check_if_bst(res.left, res.val, -math.inf))
print(iterate_in_order(re2, ""))
