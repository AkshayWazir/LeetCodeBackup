class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(node: ListNode, x: int):
    root = node
    b_mem, mem, flag, f1 = None, None, False, False
    if node.val >= x:
        mem, flag = node, True
    while node is not None and node.next is not None:
        if node.next.val >= x and mem is None:
            b_mem, mem = node, node.next
            flag = True
        elif node.next.val < x and flag:
            tn, ptn = node.next, node
            ptn.next, tn.next = tn.next, mem
            if b_mem is not None:
                b_mem.next = tn
                b_mem = b_mem.next
            else:
                root = tn
                b_mem = tn
            node = b_mem
        node = node.next
    return root


arr = [5, 1, 2, 3, 4, 1, 5, 2, 3, 6, 9, 1, 2, 5, 3]
n = ListNode(arr[0])
ro = n
for i in arr:
    n.next = ListNode(i)
    n = n.next
res = partition(ro.next, 5)
