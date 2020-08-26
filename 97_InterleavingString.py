def is_interleave(s1, s2, s3):
    def recur(w1, i, w2, j, w3, k, mem):
        if i == len(w1):
            return w2[j:] == w3[k:]
        if j == len(w2):
            return w1[i:] == w3[k:]
        if mem[i][j] >= 0:
            return True if mem[i][j] == 1 else False
        ans = False
        if (w3[k] == w1[i] and recur(w1, i + 1, w2, j, w3, k + 1, mem)) \
                or w3[k] == w2[j] and recur(w1, i, w2, j + 1, s3, k + 1, mem):
            ans = True
        mem[i][j] = 1 if ans else 0
        return ans

    memo = [[False for i in range(len(s2))] for _ in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            memo[i][j] = -1
    return recur(s1, 0, s2, 0, s3, 0, memo)


test_cases = [
    [
        "aabcc",
        "dbbca",
        "aadbbcbcac",
        True
    ],
    [
        "aabcc",
        "dbbca",
        "aadbbbaccc",
        False
    ]
]

for a, b, c, d in test_cases:
    if is_interleave(a, b, c) != d:
        print(is_interleave(a, b, c))
        print("Failed !!")
    else:
        print("Passed")
