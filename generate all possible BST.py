from itertools import permutations


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert_into_bst(node, ele):
    if ele < node.val:
        if node.left is not None:
            insert_into_bst(node.left, ele)
        else:
            node.left = TreeNode(ele)
    else:
        if node.right is not None:
            insert_into_bst(node.right, ele)
        else:
            node.right = TreeNode(ele)


def generate_array(node):
    queue = [node]
    res = []
    while len(queue) != 0:
        if queue[0] is not None:
            res.append(queue[0].val)
            queue.append(queue[0].left)
            queue.append(queue[0].right)
        else:
            res.append(queue[0])
        queue.pop(0)
    while res[len(res) - 1] is None:
        res.pop()
    return res


n = int(input("___ enter Number"))
arr = [i + 1 for i in range(n)]
perms = list(permutations(arr))
master_arr = []
ms2 = []
if n == 0:
    print([])

for j in perms:
    node = TreeNode(j[0])
    for i in range(1, len(j)):
        insert_into_bst(node, j[i])
    res = generate_array(node)
    if res not in master_arr:
        ms2.append(node)
        master_arr.append(res)
