def add_binary(a, b):
    res = []
    carry = 0
    while a or b or carry:
        carry += (a or [0]).pop() + (b or [0]).pop()
        res.append(carry & 1)
        carry = carry >> 1
    return res[::-1]


def add_nega_binary(a, b):
    res = []
    carry = 0
    while a or b or carry:
        carry += (a or [0]).pop() + (b or [0]).pop()
        res.append(carry & 1)
        carry = -(carry >> 1)
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res[::-1]


print(add_nega_binary([1, 1, 1, 1, 1], [1, 0, 1]))
