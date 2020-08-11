def solve(A, B, C):
    stack = [1]
    record = []
    edge = dict()
    for i in C:
        if edge.get(i[0], -1) != -1:
            edge[i[0]].append(i[1])
        else:
            edge[i[0]] = [i[1]]
    height = 0
    while len(stack) != 0:
        height += 1
        record = [j for j in stack]
        for i in range(len(stack)):
            if edge.get(stack[0], -1) == -1:
                stack.pop(0)
                continue
            stack += edge.get(stack[0])
            stack.pop(0)
    var = max([B[i - 1] if A[i - 1] > B[i - 1] else A[i - 1] for i in record])
    return var + height if height > var else var


ta = [0, 0, 0, 5, 3, 5, 5]
tb = [30, 20, 3, 5, 5, 5, 5]
tc = [
    [1, 2],
    [1, 3],
    [2, 4],
    [2, 5],
    [3, 6],
    [3, 7]
]
print(solve(ta, tb, tc))
