from makeBST import make_bst


def morris_in_order(node):
    current = node
    while current is not None:
        if current.left is None:
            print(current.val)
            current = current.right
        else:
            temp = current.left
            while temp.right is not None or temp.right != current:
                temp = temp.right
            if temp.right is None:
                temp.right = current
                current = current.left
            else:
                temp.right = None
                print(current.val)
                current = current.right


res = make_bst(0, 8, [1, 2, 3, 4, 5, 6, 7, 8, 9])
morris_in_order(res)
