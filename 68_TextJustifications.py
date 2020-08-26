def pack_greedy(array, max_w):
    def get_arr_size(arr):
        s = 0
        for k in arr:
            s += len(k) + 1
        return s - 1

    def justify(arr, cate):
        if cate >= 0:
            total_space = max_w - (get_arr_size(arr) - (len(arr) + 1))
            interval = total_space // (len(arr) - 1)
            extra = total_space % interval
            line = ""
            for word in arr:
                if len(line) == 0:
                    line += word
                else:
                    ex = 1 if extra > 0 else 0
                    line += " " * (interval + ex) + word
                    extra -= 1
        else:
            line = ""
            for word in arr:
                if len(line) == 0:
                    line += word + " "
                else:
                    line += word + " "
            if len(line) < max_w:
                line += " " * (max_w - len(line))
        return line

    master, temp = [], []
    for i in range(len(array)):
        if get_arr_size(temp) + len(array[i]) < max_w:
            temp.append(array[i])
        else:
            master.append([ele for ele in temp])
            temp = [array[i]]
    if len(temp) != 0:
        master.append([ele for ele in temp])

    for i in range(len(master)):
        if len(master[i]) == 1 or i == len(master) - 1:
            master[i] = justify(master[i], -1)
        else:
            master[i] = justify(master[i], 0)

    return master


def fullJustify(self, words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return res + [' '.join(cur).ljust(maxWidth)]


testcases = [
    [
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],
        20
    ],
    [
        ["This", "is", "an", "example", "of", "text", "justification."],
        16
    ]
]
for words, c in testcases:
    for l in pack_greedy(words, c):
        print(l)
    print("__ " * 10)
