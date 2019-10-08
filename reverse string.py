def reverse(index):
    if index == len(s)//2:
        return
    reverse(index + 1)
    s[index], s[len(s) - index - 1] = s[len(s) - index - 1], s[index]


s = list("HelloWorld")
reverse(0)
print(s)
