def f_l_p_s_s(string):
    dp = [[0 for i in range(len(string))] for j in range(len(string))]
    max_len = 1
    for i in range(len(string)):
        dp[i][i] = 1
        if i + 1 < len(string):
            dp[i][i + 1] = 2 if string[i] == string[i + 1] else 0
    for i in range(2, len(string)):
        for j in range(len(string) - i):
            if string[j] != string[j + i]:
                dp[j][j + i] = max(dp[j + 1][j + i], dp[j][j + i - 1])
            else:
                dp[j][j + i] = max(dp[j][j + i - 2], dp[j][j + i - 1]) + 2
    return dp[0][len(dp) - 1]


res = ["turborotator", "ababad"]

for i in res:
    print(f_l_p_s_s(i))
