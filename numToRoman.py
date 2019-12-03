def to_roman(num):
    nums = [1, 5, 10, 50, 100, 500, 1000]
    roman = ["I", "V", "X", "L", "C", "D", "M"]
    res = ""
    while num > 0:
        for i in range(-1, -len(nums) - 1, -1):
            if -3 < i <= -1:
                if nums[i] <= num:
                    res += roman[i]
                    num -= nums[i]
                    break
                elif num >= nums[-1] - nums[-3]:
                    res += roman[-3] + roman[-1]
                    num -= nums[-1] - nums[-3]
                    break
                if nums[i - 1] <= num:
                    res += roman[i - 1]
                    num -= nums[i - 1]
                    break
                elif num >= nums[-2] - nums[-3]:
                    res += roman[-3] + roman[-2]
                    num -= nums[-2] - nums[-3]
                    break
            elif -5 < i <= -3:
                if nums[i] <= num:
                    res += roman[i]
                    num -= nums[i]
                    break
                elif num >= nums[-3] - nums[-5]:
                    res += roman[-5] + roman[-3]
                    num -= nums[-3] - nums[-5]
                    break
                if nums[i - 1] <= num:
                    res += roman[i - 1]
                    num -= nums[i - 1]
                    break
                elif num >= nums[-4] - nums[-5]:
                    res += roman[-5] + roman[-4]
                    num -= nums[-4] - nums[-5]
                    break
            elif -7 < i <= -5:
                if nums[i] <= num:
                    res += roman[i]
                    num -= nums[i]
                    break
                elif num >= nums[-5] - nums[-7]:
                    res += roman[-7] + roman[-5]
                    num -= nums[-5] - nums[-7]
                    break
                if nums[i - 1] <= num:
                    res += roman[i - 1]
                    num -= nums[i - 1]
                    break
                elif num >= nums[-6] - nums[-7]:
                    res += roman[-7] + roman[-6]
                    num -= nums[-6] - nums[-7]
                    break
    return res


a = int(input())
print(to_roman(a))
