class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def link_list(node_a, node_b):
    na = ""
    while node_a is not None:
        na += str(node_a.val)
        node_a = node_a.next
    nb = ""
    while node_b is not None:
        nb += str(node_b.val)
        node_b = node_b.next
    res = int(na) + int(nb)
    res = list(str(res))
    child = ListNode(int(res.pop()))
    while len(res) != 0:
        child = ListNode(int(res.pop()), child)
    return child

a = ListNode()
