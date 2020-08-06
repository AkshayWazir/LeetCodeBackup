def get_length(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    count = 1
    max_count = 1
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1
    return max_count


a = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
b = [2, 2, 2, 2, 2]
c = [1, 2, 3, 4, 5, 6, 7]
print(get_length(a))
print(get_length(b))
print(get_length(c))
