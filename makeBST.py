class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def make_bst(start, end, arr):
    if start > end:
        return None
    if len(arr) == 1:
        return Node(arr[0])
    mid = (start + end) // 2
    a = Node(arr[mid])
    a.left = make_bst(start, mid - 1, arr)
    a.right = make_bst(mid + 1, end, arr)
    return a


ar = [1, 2, 3, 4, 5, 6, 7]
res = make_bst(0, len(ar) - 1, ar)

print(res)
