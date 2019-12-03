def hey_stack(hey, pin):
    try:
        return hey.index(pin)
    except:
        return -1


word = input()
target = input()
print(hey_stack(word, target))
