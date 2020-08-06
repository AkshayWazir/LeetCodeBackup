def match_word(s, p):
    s = list(s)
    p = list(p)
    i = 0
    while i < len(s) - 1:
        if s[i + 1] == s[i]:
            s[i] += s[i + 1]
            s.pop(i + 1)
        i += 1
    i = 0

    return True


print(match_word("mississipi", "mic*s*.s*i.i"))
