def inorder_travesal(node, result):
    if node.left is not None:
        result = inorder_travesal(node.left, result)
        result.append(node.val)
        result = inorder_travesal(node.right, result)
        return result
    elif node.right is not None:
        result.append(node.val)
        result = inorder_travesal(node.right, result)
        return result
    else:
        result.append(node.val)
        return result


