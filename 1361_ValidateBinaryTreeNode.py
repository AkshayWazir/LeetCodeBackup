def validate(n, left_c, right_c):
    def recur(node, lc, rc):
        nonlocal memory, fail
        if node == -1 or fail:
            return
        else:
            if memory[node]:
                memory[node] = False
                fail = True
                return
            else:
                memory[node] = True
            recur(lc, left_c[lc], right_c[lc])
            recur(rc, left_c[rc], right_c[rc])

    memory = [False for i in range(n)]
    fail = False
    f_dict = dict()
    for i in range(n):
        f_dict[left_c[i]] = 0
        f_dict[right_c[i]] = 0
    root_count = 0
    for i in range(n):
        if f_dict.get(i, -1) == -1:
            root_count += 1
            recur(i, left_c[i], right_c[i])
    return False not in memory and not fail and root_count == 1


test_cases = [
    [
        4,
        [1, -1, 3, -1],
        [2, 3, -1, -1],
        False
    ],
    [
        4,
        [1, -1, 3, -1],
        [2, -1, -1, -1],
        True
    ],
    [
        2,
        [1, 0],
        [-1, -1],
        False
    ],
    [
        6,
        [1, -1, -1, 0, -1, -1],
        [2, -1, -1, 5, -1, -1],
        False
    ],
    [
        10,
        [0, 7, 4, 7, 2, 8, 7, 8, 3, 6],
        [0, 8, 5, 4, 8, 2, 3, 1, 2, 1],
        False
    ],
    [
        6,
        [1, -1, -1, 4, -1, -1],
        [2, -1, -1, 5, -1, -1],
        False
    ],
    [
        2,
        [-1, 0],
        [-1, -1],
        True
    ]
]

for test in test_cases:
    res = "Pass" if validate(test[0], test[1], test[2]) == test[-1] else "Failed"
    print(res)
