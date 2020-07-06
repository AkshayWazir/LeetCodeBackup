def sqrt(number):
    num1, num2 = 0, number
    while True:
        middle = (num1 + num2) // 2
        if num1 ** 2 == number:
            return num1
        elif num2 ** 2 == number:
            return num2
        elif num1 == num2 - 1:
            return num1
        if middle ** 2 < number:
            num1 = middle
        elif middle ** 2 > number:
            num2 = middle
        elif middle ** 2 == number:
            return middle
        else:
            return num1


print(sqrt(1))
