def make_palindrome(word):
    def check_palindrome(temp_word):
        if len(temp_word) == 1:
            return True
        elif len(temp_word) == 0:
            return False
        for i in range(len(temp_word) // 2):
            if temp_word[i] != temp_word[-(i + 1)]:
                return False
        return True

    def recur(current, chosen):
        if len(current) == 0:
            nonlocal master
            master.append([k for k in chosen])
            return
        for i in range(len(current)):
            if check_palindrome(current[:i + 1]):
                chosen.append(current[:i + 1])
                recur(current[i + 1:], chosen)
                chosen.pop()

    master = []
    recur(word, [])
    return master


for i in make_palindrome("aab"):
    print(i)
