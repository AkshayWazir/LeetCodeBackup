def count_possibility(s, arr):
    if len(s) == 0 and len("".join(arr)) == const:
        global count
        count += 1
    elif len(s) != 0:
        count_possibility(s[1:], arr + [s[0]] if 1 <= int(s[0]) <= 26 else [])
        if len(s) >= 2:
            count_possibility(s[2:], arr + [s[0] + s[1]] if 1 <= int(s[0] + s[1]) <= 26 else [])


def dp_solution(s):
    if s is None or len(s) == 0:
        return 0
    n = len(s)
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1 if s[0] != 0 else 0
    for i in range(2, n + 1):
        first = int(s[i - 1:i])
        second = int(s[i - 2:i])
        if 1 <= first <= 9:
            dp[i] += dp[i - 1]
        if 10 <= second <= 26:
            dp[i] += dp[i - 2]
    return dp[n]


var = "2246564187878577871875271817871781718756112271724127215"
count, const = 0, len(var)
# count_possibility(var, [])
print(dp_solution(var))
print(count)
