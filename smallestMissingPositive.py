def find_spi(nums):
    if len(nums) == 0:
        return 1
    elif max(nums) < 0:
        return 1
    i = 1
    while i != nums:
        if i not in nums:
            return i
        i += 1
    else:
        return max(nums) + 1


arr = list(map(int, input().split()))
print(find_spi(arr))
