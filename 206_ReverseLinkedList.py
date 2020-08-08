class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rev(node):
    if node.next is None:
        return [node, node]
    else:
        res = rev(node.next)
        res[0].next = node
        return [node, res[1]]


arr = [1, 2, 3, 4, 5, 6]
head = ListNode(arr[0])
root = head
for i in range(1, len(arr)):
    head.next = ListNode(arr[i])
    head = head.next

if root is None:
    print(None)
res1 = rev(head)
res1[0].next = None
print(res1[1])
