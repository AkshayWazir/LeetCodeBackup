import math


def find_min(board, hand):
    def filter_balls(balls):
        if len(balls) == 0:
            return balls
        rtr = []
        cur, c = balls[0], 0
        for i, val in enumerate(balls):
            if val == cur:
                c += 1
            else:
                if c >= 3:
                    rtr = [i - c, c]
                cur, c = val, 1
        if c >= 3:
            rtr = [len(balls) - c - 1, c]

        if len(rtr) > 0:
            for i in range(rtr[1]):
                balls.pop(rtr[0])
            return filter_balls(balls)
        else:
            return balls

    def recur(row, cur, count):
        nonlocal mem
        if mem.get("".join(row), -1) != -1:
            return mem.get("".join(row))
        if len(cur) == 0 or len(row) == 0:
            if len(row) == 0:
                return count
            else:
                return math.inf
        t_res = []
        for j in range(len(cur)):
            for i in range(len(row)+1):
                temp = cur.pop(j)
                row.insert(i, temp)
                res = recur([s for s in filter_balls([k for k in row])], cur, count + 1)
                mem["".join(row)] = res
                t_res.append(res)
                row.pop(i)
                cur.insert(j, temp)
        return min(t_res) if len(t_res) != 0 else math.inf

    mem = dict()
    re1 = recur(list(board), list(hand), 0)
    return re1 if re1 != math.inf else -1


print(find_min("WWRRBBWW", "WRBRW"))
