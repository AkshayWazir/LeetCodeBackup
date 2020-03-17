from makeTree import make_tree


def getTarget(node, tar):
    res1, res3 = False, False
    if node.left is not None:
        res1 = getTarget(node.left, tar - node.val)
    if node.right is not None:
        res3 = getTarget(node.right, tar - node.val)

    if node.left is None and node.right is None and tar - node.val == 0:
        return True
    return res1 or res3


res = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
nod = make_tree(res)
print(getTarget(nod, 22))
