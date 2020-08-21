class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head: ListNode, k: int) -> ListNode:
    def rev_m_to_n(head: ListNode, m: int, n: int) -> ListNode:
        def rev(node: ListNode, count: int):
            if count == 0 or node.next is None:
                return [node, node, node.next]
            else:
                temp_res = rev(node.next, count - 1)
                temp_res[0].next = node
                return [node, temp_res[1], temp_res[2]]

        if head is None:
            return head
        times = n - m
        if m == 1:
            res1 = rev(head, times)
            root, res1[0].next = res1[1], res1[2]
            return root
        else:
            root = head
            while m > 2:
                head, m = head.next, m - 1
            res2 = rev(head.next, times)
            res2[0].next, head.next = res2[2], res2[1]
            return root

    root, count = head, 0
    while head is not None:
        head = head.next
        count += 1
    for i in range(count // k):
        root = rev_m_to_n(root, i * k + 1, (i * k) + k)
    return root
