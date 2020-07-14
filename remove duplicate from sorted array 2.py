def remove_duplicate_2(nums):
    memory, visits, i = -1, 0, 0
    while i < len(nums):
        if nums[i] != memory:
            memory, visits = nums[i], 1
            i += 1
        elif nums[i] == memory:
            if visits < 2:
                visits += 1
                i += 1
            else:
                nums.pop(i)
    return len(nums)


print(remove_duplicate_2([]))
