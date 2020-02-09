def find(node, target, count, res, go):
    if node is None:
        return res
    elif count == 0:
        res.append(node.val)
        return res

    if node.val == target:
        if node.left is not None:
            res = find(node.left, target, count - 1, res, True)
        if node.right is not None:
            res = find(node.right, target, count - 1, res, True)
    elif go:
        if node.left is not None:
            res = find(node.left, target, count - 1, res, True)
        if node.right is not None:
            res = find(node.right, target, count - 1, res, True)
    else:
        if node.left is not None:
            res = find(node.left, target, count, res, go)
            master[str(node.left)] = str(node.val)
        if node.right is not None:
            res = find(node.right, target, count, res, go)
            master[str(node.right)] = str(node.val)
    return res

master = {}
