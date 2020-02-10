import makeBST


def give_in_order(node):
    if node is None:
        return []
    return give_in_order(node.left) + [node.val] + give_in_order(node.right)


arr = [1, 2, 3, 4, 5, 6, 7]
res = makeBST.make_bst(0, len(arr) - 1, arr)
print(give_in_order(res))
