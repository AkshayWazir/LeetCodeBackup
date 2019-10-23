def find_range(nums, target):
    if len(nums) == 0 or target not in nums:
        return [-1, -1]
    s, e = 0, len(nums) - 1
    while True:
        if nums[s] < target < nums[e]:
            s, e = s + 1, e - 1
        elif nums[s] < target:
            s += 1
        elif nums[e] > target:
            e -= 1
        elif s > e:
            res = [-1, -1]
            return res
        else:
            res = [s, e]
            return res


arr = list(map(int, input().split()))
range_obj = int(input())
print(find_range(arr, range_obj))
