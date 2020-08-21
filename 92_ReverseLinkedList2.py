class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def give_linked_list(arr):
    head = ListNode(arr[0])
    root = head
    for i in range(1, len(arr)):
        head.next = ListNode(arr[i])
        head = head.next
    return root


def give_res(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next


rt = give_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
give_res(rev_m_to_n(rt, 5, 12))
print()
