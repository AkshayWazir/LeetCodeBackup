from math import ceil, log2


class SegTree:
    def __init__(self, array):
        self.array = array
        # core formula for array size
        x = int(ceil(log2(len(array))))
        max_size = 2 * int(2 ** x)
        self.sg_tree = [0] * max_size

        def build(start, end, node):
            if start == end:
                self.sg_tree[node] = self.array[start]
                return self.sg_tree[node]
            else:
                mid = (start + end) // 2
                self.sg_tree[node] = build(start, mid, node * 2) + build(mid + 1, end, node * 2 + 1)
                return self.sg_tree[node]

        build(0, len(array) - 1, 1)

    def query(self, start, end):
        def search(left, right, s, e, n):
            if s <= left <= right <= e:
                return self.sg_tree[n]
            elif left <= s <= right or left <= e <= right:
                mid = (left + right) // 2
                return search(left, mid, s, e, 2 * n) + search(mid + 1, right, s, e, 2 * n + 1)
            else:
                return 0

        return search(0, len(self.array) - 1, start - 1, end - 1, 1)

    def update(self, i, val):
        dif = val - self.array[i - 1]
        self.array[i - 1] = val

        def upd(start, end, pos, ad, count):
            if start > pos or end < pos:
                return
            self.sg_tree[count] += ad
            if start != end:
                mid = (start + end) // 2
                upd(start, mid, pos, ad, 2 * count)
                upd(mid + 1, end, pos, ad, 2 * count + 1)

        upd(0, len(self.array) - 1, i-1, dif, 1)


n = SegTree([i + 1 for i in range(9)])
print(n.sg_tree)
print(n.query(6, 9))
n.update(8, 5)
print(n.sg_tree)
print(n.query(6, 9))
