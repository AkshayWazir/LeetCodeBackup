class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rec_solution(node, k, temp_count):
    if node.next is None:
        return [k % temp_count, node]
    else:
        res = rec_solution(node.next, k, temp_count + 1)
        if res[0] == 0:
            res.append(node.next)
            node.next = None
        res[0] -= 1
        return res


result = rec_solution(node, k, 1)
result[1].next = node
return result[2]
