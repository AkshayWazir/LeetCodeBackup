import heapq


def max_events(A):
    A.sort(reverse=1)
    h = []
    res = d = 0
    while A or h:
        if not h:
            d = A[-1][0]
        while A and A[-1][0] <= d:
            heapq.heappush(h, A.pop()[1])
        heapq.heappop(h)
        res += 1
        d += 1
        while h and h[0] < d:
            heapq.heappop(h)
    return res


print(max_events([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]))
