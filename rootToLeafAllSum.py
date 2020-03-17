def get_sum(node, curr):
    if node.left is None and node.right is None:
        curr += str(node.val)
        nonlocal papasum
        papasum += int(curr)
    else:
        get_sum(node.left, curr + str(node.val))
        get_sum(node.right, curr+ str(node.val))


papasum = 0
get_sum()