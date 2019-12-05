def get_the_3_sum(arr, target):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    mod, ans, keys = 10 ** 9 + 7, 0, list(freq.keys())
    keys.sort()
    for i in range(len(keys)):
        a = keys[i]
        if a * 3 > target:
            break
        for j in range(i, len(keys)):
            b = keys[j]
            c = target - a - b
            if c < b:
                break
            if c not in freq:
                continue
            if a == b:
                if b == c:
                    if freq[a] > 2:
                        # here it divide by 6 because of the combinations formula which is 3! in case of 3 same elements
                        # and 2! in case of 2 same elements
                        ans += freq[a] * (freq[a] - 1) * (freq[a] - 2) // 6
                else:
                    if freq[a] > 1:
                        ans += freq[a] * (freq[a] - 1) * freq[c] // 2
            else:
                if b == c:
                    if freq[b] > 1:
                        ans += freq[a] * freq[b] * (freq[b] - 1) // 2
                else:
                    ans += freq[a] * freq[b] * freq[c]
        ans %= mod
    return ans


# [1,2,3,3,1]
# 5 - > 2

print(get_the_3_sum([1, 2, 3, 3, 1], 5))
