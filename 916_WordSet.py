from collections import Counter


def get_set(A, B):
    count = Counter()
    for b in B:
        count = count | Counter(b)
    return [a for a in A if Counter(a) & count == count]


print(get_set(["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"]))
