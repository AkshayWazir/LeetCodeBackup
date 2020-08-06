def merger(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()


arr1 = [1, 3, 5, 7, 0, 0, 0]
arr2 = [2, 4, 6]
print(merger(arr1, len(arr1), arr2, len(arr2)))
print(arr1)
print(arr2)
