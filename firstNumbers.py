def get_number(word):
    if len(word) == 0:
        return 0
    words = word.split()
    if len(words) == 0:
        return 0
    correct = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 43, 45]
    if words[0][0] == "-" or words[0][0] == "+" or ord(words[0][0]) in range(48, 58):
        res = [words[0][i] if ord(words[0][i]) in correct else " " for i in range(len(words[0]))]
        refined = "".join(res)
        sym = ["+", "-"]
        while refined[0] in sym and refined[1] in sym:
            refined = refined[1:]

        if refined == "+" or refined == "-":
            return 0
        res = list(map(int, refined.split()))

        if res[0] > 2 ** 31:
            return 2 ** 31
        elif res[0] < -2 ** 31:
            return -2 ** 31
        else:
            return res[0]
    else:
        return 0


text = input("Enter the text : ")
print(get_number(text))
