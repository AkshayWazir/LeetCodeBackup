def sumtoarr(arr, k):
    return list(str(int("".join(list(map(str, arr)))) + k))


def actual_method(arr, k):
    carry = 0
    k = list(map(int, list(str(k))))
    for i in range(-1, -max(len(k), len(arr)) - 1, -1):
        if -i < len(k) and -i < len(arr):
            arr[i] = carry + arr[i] + k[i]
            if arr[i] > 9:
                carry, arr[0] = 1, arr[0] % 10
            else:
                carry = 0
        elif -i > len(arr):
            arr[0] = k[i] + carry
            if arr[0] > 9:
                carry, arr[0] = 1, arr[0] % 10
            else:
                carry = 0
        else:
            arr[i] = arr[i] + carry
            
    return arr


print(actual_method([9, 9, 9, 9], 1))
