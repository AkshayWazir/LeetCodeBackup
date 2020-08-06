def break_word(s, words):
    d = [False] * len(s)
    for i in range(len(s)):
        for w in words:
            a = s[i - len(w) + 1:i + 1]
            if w == a and (d[i - len(w)] or i - len(w) == -1):
                d[i] = True
    return d[-1]


print(break_word("catsandog", ["cat", "cats", "sand", "dog", "and"]))
