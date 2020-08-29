import collections


def get_construct(tickets):
    def recur(arr, start, memory):
        nonlocal rem
        if rem.get(tuple(arr), -1) != -1:
            return rem.get(tuple(arr), -1)
        elif len(memory.get(start, [])) >= 1:
            ms, ta = 0, []
            for i in range(len(memory[start])):
                temp = memory[start].pop(i)
                tr = recur(arr + [temp], temp, memory)
                memory[start].insert(i, temp)
                if len(tr) > ms:
                    ms = len(tr)
                    ta = tr
            rem[tuple(arr)] = ta
            return ta
        else:
            return []

    rem = dict()
    mem = dict()
    for f, t in tickets:
        if mem.get(f, -1) == -1:
            mem[f] = [t]
        else:
            mem[f].append(t)
            mem[f].sort()
    res = ["JFK"]
    return recur(res, res[-1], mem)


def get_tic_optimal(tickets):
    d = collections.defaultdict(list)
    for flight in tickets:
        d[flight[0]] += flight[1],
    route = ["JFK"]

    def dfs(start='JFK'):
        nonlocal route
        if len(route) == len(tickets) + 1:
            return route
        myDsts = sorted(d[start])
        for dst in myDsts:
            d[start].remove(dst)
            route += dst,
            worked = dfs(dst)
            if worked:
                return worked
            route.pop()
            d[start] += dst,

    return dfs()


test_case = [["AXA", "EZE"], ["EZE", "AUA"], ["ADL", "JFK"], ["ADL", "TIA"], ["AUA", "AXA"], ["EZE", "TIA"], ["EZE", "TIA"], ["AXA", "EZE"], ["EZE", "ADL"], ["ANU", "EZE"], ["TIA", "EZE"],
             ["JFK", "ADL"], ["AUA", "JFK"], ["JFK", "EZE"], ["EZE", "ANU"], ["ADL", "AUA"], ["ANU", "AXA"], ["AXA", "ADL"], ["AUA", "JFK"], ["EZE", "ADL"], ["ANU", "TIA"], ["AUA", "JFK"],
             ["TIA", "JFK"], ["EZE", "AUA"], ["AXA", "EZE"], ["AUA", "ANU"], ["ADL", "AXA"], ["EZE", "ADL"], ["AUA", "ANU"], ["AXA", "EZE"], ["TIA", "AUA"], ["AXA", "EZE"], ["AUA", "SYD"],
             ["ADL", "JFK"], ["EZE", "AUA"], ["ADL", "ANU"], ["AUA", "TIA"], ["ADL", "EZE"], ["TIA", "JFK"], ["AXA", "ANU"], ["JFK", "AXA"], ["JFK", "ADL"], ["ADL", "EZE"], ["AXA", "TIA"],
             ["JFK", "AUA"], ["ADL", "EZE"], ["JFK", "ADL"], ["ADL", "AXA"], ["TIA", "AUA"], ["AXA", "JFK"], ["ADL", "AUA"], ["TIA", "JFK"], ["JFK", "ADL"], ["JFK", "ADL"], ["ANU", "AXA"],
             ["TIA", "AXA"], ["EZE", "JFK"], ["EZE", "AXA"], ["ADL", "TIA"], ["JFK", "AUA"], ["TIA", "EZE"], ["EZE", "ADL"], ["JFK", "ANU"], ["TIA", "AUA"], ["EZE", "ADL"], ["ADL", "JFK"],
             ["ANU", "AXA"], ["AUA", "AXA"], ["ANU", "EZE"], ["ADL", "AXA"], ["ANU", "AXA"], ["TIA", "ADL"], ["JFK", "ADL"], ["JFK", "TIA"], ["AUA", "ADL"], ["AUA", "TIA"], ["TIA", "JFK"],
             ["EZE", "JFK"], ["AUA", "ADL"], ["ADL", "AUA"], ["EZE", "ANU"], ["ADL", "ANU"], ["AUA", "AXA"], ["AXA", "TIA"], ["AXA", "TIA"], ["ADL", "AXA"], ["EZE", "AXA"], ["AXA", "JFK"],
             ["JFK", "AUA"], ["ANU", "ADL"], ["AXA", "TIA"], ["ANU", "AUA"], ["JFK", "EZE"], ["AXA", "ADL"], ["TIA", "EZE"], ["JFK", "AXA"], ["AXA", "ADL"], ["EZE", "AUA"], ["AXA", "ANU"],
             ["ADL", "EZE"], ["AUA", "EZE"]]
print(get_construct(test_case))
