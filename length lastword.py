def get_length(w):
    w = w.split()
    if len(w) == 0:
        return 0
    return len(w[len(w) - 1])


word = input()
print(get_length(word))
