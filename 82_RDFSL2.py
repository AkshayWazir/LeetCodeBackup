class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def function(node):
    temp = node
    while node is not None:
        if node.next is not None and node.val != node.next.val:
            node = node.next
        else:
            if node.next is None:
                node = node.next
                continue
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            node.val = "#"
    while temp.val == "#":
        temp = temp.next
    var = temp
    while temp is not None and temp.next is not None:
        if temp.next.val == "#":
            while temp.next is not None and temp.next.val == "#":
                temp.next = temp.next.next
        temp = temp.next
    return var


n = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(5, ListNode(5)))))))
print(function(n))
