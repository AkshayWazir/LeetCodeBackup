from ModelClass import Node


def make_tree(arr):
    root = Node(arr[0])
    queue = [root]
    arr.pop(0)
    while len(arr) != 0:
        for i in range(len(queue)):
            if arr[0] is not None:
                queue[0].left = Node(arr[0])
            if arr[1] is not None:
                queue[0].right = Node(arr[1])
            if queue[0] is not None:
                queue += [queue[0].left, queue[0].right]
                arr = arr[2:]
            queue.pop(0)
    return root


res = make_tree([4, 2, 6, 1, None, 5, None])
print(res)
