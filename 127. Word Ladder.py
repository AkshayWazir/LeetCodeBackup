import math


def word_ladder(init, target, options):
    def difference(opt1, opt2):
        count = 0
        for i in range(len(opt1)):
            if opt1[i] != opt2[i]:
                count += 1
        return count

    def get_least_difference(word):
        valid = []
        for pos, i in enumerate(options):
            if difference(word, i) == 1 and not memory[pos]:
                valid.append(i)
        return valid

    def recur(cur, tar, opt):
        nonlocal min_op
        if cur == tar:
            min_op = min(opt, min_op)
        elif opt == len(options):
            return
        else:
            cases = get_least_difference(cur)
            for j in cases:
                memory[options.index(j)] = True
                recur(j, tar, opt + 1)
                memory[options.index(j)] = False

    min_op = math.inf
    memory = [False for i in range(len(options))]
    recur(init, target, 1)
    if min_op == math.inf:
        return 0
    return min_op


test_cases = [
    [
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"],
        5
    ],
    [
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log"],
        0
    ]
]
for a, b, c, d in test_cases:
    print(word_ladder(a, b, c) == d)
