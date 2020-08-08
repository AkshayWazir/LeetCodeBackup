import collections


def gen(nums):
    res = [[]]
    for num, freq in collections.Counter(nums).items():
        res_len = len(res)
        for i in range(1, freq + 1):
            for r in res[:res_len]:
                res.append(r + [num] * i)
    return res


master_set = gen(sorted([1, 2, 3, 4, 5, 2, 2, 2, 3]))
for s in master_set:
    print(s)
