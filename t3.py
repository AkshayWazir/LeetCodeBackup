def func(A, B, C):
    graph = dict()
    for node, child, val in B:
        if graph.get(node, -1) == -1:
            graph[node] = [[child, val]]
        else:
            graph[node].append([child, val])

    def get_sum(node, target, ts, max_al, att):
        if node == target:
            return ts
        else:
            arr = graph.get(node, -1)
            if arr == -1:
                return
            for n in arr:
                if att <= max_al:
                    res1 = get_sum(n[0], target, ts + 0, max_al, att + 1)
                    res2 = get_sum(n[0], target, ts + n[1], max_al, att)
                else:
                    res1 = get_sum(n[0], target, ts + n[1], max_al, att)
                    res2 = get_sum(n[0], target, ts + n[1], max_al, att)
                if res1 is not None and res2 is not None:
                    return max(res1, res2)

    final = list()
    for i in range(1, A + 1):
        for j in range(A):
            res3 = get_sum(1, i, 0, C, 0)
            final.append(res3)
    print(final)


ta = 5
tb = [
    [1, 2, 11],
    [1, 3, 5],
    [2, 4, 3],
    [2, 5, 14]
]
tc = 1
func(ta, tb, tc)
