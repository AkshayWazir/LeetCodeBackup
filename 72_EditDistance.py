def min_distance(word1, word2, cache={}):
    if not word1 and not word2:  # case when both words are empty
        return 0
    if not len(word1) or not len(word2):  # case when either of them is empty
        return len(word1) or len(word2)  # return the size of word which is not empty = insert operations
    if word1[0] == word2[0]:  # if words match with one another just move on without any operation
        return min_distance(word1[1:], word2[1:])
    if (word1, word2) not in cache:  # if the branch is visited first time
        inserted = 1 + min_distance(word1, word2[1:])  # insert operation
        deleted = 1 + min_distance(word1[1:], word2)  # delete operation
        replaced = 1 + min_distance(word1[1:], word2[1:])  # replace operation
        cache[(word1, word2)] = min(inserted, deleted, replaced)  # return the least of them all
    return cache[(word1, word2)]  # return the cached solution because we have been here earlier


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
    if min_distance(f, s) == r:
        print("Pass !!")
    else:
        print("Failed")
