def rev_word(s):
    s = s.split()
    return " ".join([s[::-1] for i in s])
