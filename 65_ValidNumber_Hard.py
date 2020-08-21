def check_valid(word: str) -> bool:
    word = "".join(word.split())
    if not word:
        return False
    check = [False] * len(word)
    nums = [48, 57]
    chars = ['+', '-', '*', '/', '.']
    check[0] = True if word[0] in chars or ord(word[0]) in range(nums[0], nums[1] + 1) else False
    ef = False
    for i in range(1, len(word)):
        if word[i] == 'e':
            if ef:
                return False
            else:
                ef = word[i] == 'e'
                check[i] = check[i - 1]
        elif ord(word[i]) in range(nums[0], nums[1] + 1):
            check[i] = check[i - 1]
        elif word[i] == '.':
            if ef:
                return False
            else:
                check[i] = check[i - 1]
        elif word[i] in chars:
            check[i] = check[i - 1]
        else:
            return False

    if len(word) == 1 and (word[0] in chars[:len(chars) - 1] or word[0] == 'e'):
        return False
    return check[len(check) - 1]


cases = ["", "45", "485e4", " -4.85e45  ", "4-45e4.5", "-", "+", "."]
for case in cases:
    print(case, check_valid(case))
