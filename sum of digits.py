def add_digit(number):
    temp = sum(list(map(int, list(str(number)))))
    if temp != number:
        res = add_digit(temp)
    else:
        return temp
    return res


print(add_digit(12345))
