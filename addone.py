def add_one(array):
    carry = 1
    for i in range(-1, -len(array) - 1, -1):
        temp = carry + array[i]
        carry = 1 if temp > 9 else 0
        array[i] = temp % 10 if temp > 9 else temp
    if carry == 1:
        array.insert(0, 1)
    return array


print(add_one([4,0]))
