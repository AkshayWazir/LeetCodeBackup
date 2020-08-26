from collections import Counter


def min_window(s, t):
    need, missing = Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]


test_cases = [
    [
        "ADOBECODEBANC",
        "ABC",
        "BANC"
    ]
]

for w1, w2, ans in test_cases:
    if min_window(w1, w2) == ans:
        print("Passed !!")
    else:
        print("Failed !!")
