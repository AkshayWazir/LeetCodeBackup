def reverse(a):
    if int(str(a)[::-1]) > ((2**31) - 1):
        return 0
    else:
        return int(str(a)[::-1])


print(reverse(-555555))
