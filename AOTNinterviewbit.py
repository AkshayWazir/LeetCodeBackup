def get_the_arr(number):
    carry = 1
    result = []
    last_zero = 0
    for i in range(-1, -len(number) - 1, -1):
        if number[i] == 0 and last_zero == 0:
            last_zero = i
        if number[i] + carry > 9:
            result.insert(0, (number[i] + carry) % 10)
            carry = 1
        else:
            if number[i] + carry != 0:
                last_zero = 0
            result.insert(0, (number[i] + carry) % 10)
            carry = 0
    if carry == 1:
        result.insert(0, 1)
    if len(result) == 0:
        return [1]
    elif last_zero != 0:
        return result[len(result) + last_zero + 1:]
    else:
        return result


def chaaalu(num):
    result = int("".join(list(map(str, num)))) + 1
    return list(map(int, list(str(result))))


a = list(map(int, list(input())))
print(chaaalu(a))
