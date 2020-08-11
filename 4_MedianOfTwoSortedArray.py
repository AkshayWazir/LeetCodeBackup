def find_median(nums1, nums2):
    res = nums1 + nums2
    res.sort()
    if len(res) % 2 == 0:
        return (res[len(res) // 2 - 1] + res[len(res) // 2]) / 2
    else:
        return res[len(res) // 2]


print(find_median([3], [-2, -1]))
