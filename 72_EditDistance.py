from math import inf


def min_distance(word1, word2):
    if not word1 and not word2:
        return 0
    if not word1:
        return len(word2)
    if not word2:
        return len(word1)
    if word1[0] == word2[0]:
        return min_distance(word1[1:], word2[1:])
    insert = 1 + min_distance(word1, word2[1:])
    delete = 1 + min_distance(word1[1:], word2)
    replace = 1 + min_distance(word1[1:], word2[1:])
    return min(insert, replace, delete)


test_cases = [
    (
        "intention",
        "execution",
        5
    ),
    (
        "horse",
        "ros",
        3
    )
]
for f, s, r in test_cases:
    if min_distance(list(f), list(s)) == r:
        print("Pass !!")
    else:
        print("Failed")
