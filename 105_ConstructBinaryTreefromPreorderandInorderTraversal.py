class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    def recur(node, l_sub, r_sub, p_ord):
        nonlocal mem
        if len(l_sub) == 0 and len(r_sub) == 0:
            return node
        else:
            if len(l_sub) != 0:
                mem[preorder.index(p_ord[0])] = True
                node.left = recur(
                    TreeNode(p_ord[0]),
                    l_sub[:l_sub.index(p_ord[0])],
                    l_sub[l_sub.index(p_ord[0]) + 1:],
                    p_ord[1:]
                )

            if len(r_sub) == 0:
                return node
            k = 0

            while mem[k]:
                k += 1
            val = preorder[k]
            mem[k] = True
            node.right = recur(
                TreeNode(val),
                r_sub[:r_sub.index(val)],
                r_sub[r_sub.index(val) + 1:],
                p_ord[p_ord.index(val) + 1:]
            )
            return node

    root = TreeNode(preorder[0])
    mem = [False for i in range(len(preorder))]
    mem[0] = True
    node_t = root
    recur(
        node_t,
        inorder[:inorder.index(root.val)],
        inorder[inorder.index(root.val) + 1:],
        preorder[1:]
    )
    return root


t1 = [1, 2, 4, 8, 5, 3, 6, 7, 9]
t2 = [8, 4, 2, 5, 1, 6, 3, 9, 7]

build_tree(t1, t2)
