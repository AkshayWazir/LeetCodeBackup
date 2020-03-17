import makeBST
from makeTree import make_tree


def give_in_order(node):
    if node is None:
        return []
    return give_in_order(node.left) + [node.val] + give_in_order(node.right)


arr = [4, 2, 6, 1, None, 5, None]
res = make_tree(arr)
print(give_in_order(res))
