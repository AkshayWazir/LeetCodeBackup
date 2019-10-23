def search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[end]:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


arr = list(map(int, input().split()))
target1 = int(input())
print(search(arr, target1))
