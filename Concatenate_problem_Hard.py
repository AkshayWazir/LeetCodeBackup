import itertools


def concat_check(word, arr_words):
    if len(arr_words) == 0 or len(word) == 0:
        return []
    all_permut = itertools.permutations(arr_words, len(arr_words))
    word_box = []
    pos = []
    for i in all_permut:
        word_box.append("".join(i))
    spec_num = len(arr_words) * len(arr_words[0])
    for j in range(0, len(word) - spec_num + 1):
        if word[j:j + spec_num] in word_box:
            pos.append(j)
    return pos

# this one worked
def concat_check_eff(word, arr_words):
    result = []
    arr_words.sort()
    for i in range(0, len(word) - (len(arr_words) * len(arr_words[0])) + 1):
        ele = word[i:i + len(arr_words[0])]
        if ele in arr_words:
            temp = []
            for j in range(len(arr_words)):
                temp.append(word[i + j * len(arr_words[0]):i + j * len(arr_words[0]) + len(arr_words[0])])
            temp.sort()
            if temp == arr_words:
                result.append(i)
    return result


word1 = input()
word_arr = input().split()
print(concat_check_eff(word1, word_arr))
