def find_in_rotated(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < nums[left]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        elif nums[mid] == nums[left]:
            if nums[mid] != nums[right]:
                left = mid + 1
            else:
                left = left + 1
    return False


def binary_search(array, target):
    start, end, middle = 0, len(array), len(array) // 2
    while start < end:
        if array[middle] == target:
            return [1, middle]
        elif array[start] == target:
            return [1, start]
        if array[middle] < target:
            start = middle + 1
        elif array[middle] > target:
            end = middle
        middle = (start + end) // 2
    if start >= end:
        return [-1, start]


print(find_in_rotated([2, 3, 3, 0, 0, 1, 2], 3))
