

test_cases = [
    [
        [3, 5, 1, 2, 4],
        1,
        4
    ],
    [
        [3, 1, 5, 4, 2],
        2,
        -1
    ]
]

for f1, f2, ans in test_cases:
    if find_group(f1, f2) == ans:
        print("Passed")
    else:
        print("Failed")
