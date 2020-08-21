def check_wildcard(s: str, p: str) -> bool:
    def recur(actual, wild):
        nonlocal memory
        pos = str(0) + "->" + str(l - len(actual) - 1)
        if memory.get(pos, False):
            return True
        if len(actual) == 0 and len(wild) == 0:
            return True
        elif len(actual) == 0 and wild[0] == '*':
            return memory.get(l - len(actual), recur(actual, wild[1:]))
        elif len(wild) == 0 or len(actual) == 0:
            return False
        elif actual[0] == wild[0] or wild[0] == '?':
            memory[pos] = True
            return memory.get(l - len(actual), recur(actual[1:], wild[1:]))
        elif wild[0] == '*':
            return memory.get(l - len(actual), recur(actual[1:], wild) or recur(actual, wild[1:]))
        else:
            memory[pos] = False
            return False

    l = len(s) + 1
    memory = dict()
    return recur(s, p)


def correct_dp(k, l):
    def helper(s, p, start_s, start_p):
        nonlocal memo
        if (start_s, start_p) in memo:  # If the computation is already done, directly return the cached result
            return memo[(start_s, start_p)]
        res = False
        if start_s == len(s) and start_p == len(p):
            res = True
        elif start_s == len(s):
            res = p[start_p] == '*' and helper(s, p, start_s, start_p + 1)
        elif start_p == len(p):
            res = False
        elif p[start_p] == '*':
            res = helper(s, p, start_s + 1, start_p) or helper(s, p, start_s, start_p + 1)
        elif p[start_p] == '?' or p[start_p] == s[start_s]:
            res = helper(s, p, start_s + 1, start_p + 1)
        else:
            res = False
        memo[(start_s, start_p)] = res  # Before returning the result, cache it !
        return res

    memo = {}
    helper(k, l, 0, 0)


test_cases = [
    ["acdcb", "a*c?b", False],
    ["aa", "a", False],
    ["", "*", True],
    ["aabcd", "a*b?d", True],
    ["cb", "?a", False],
    ["aa", "*", True],
    ["adceb", "*a*b", True],
    ["aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab", "*ab***ba**b*b*aaab*b", True],
    ["mississippi", "m??*ss*?i*pi", False]
]
for a, t, r in test_cases:
    print("pass" if correct_dp(a, t) == r else "Failed")
