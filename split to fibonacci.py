# we need to 123,456,579
def split_it(word, sequence, cons):
    if len(word) > 0:
        if len(sequence) >= 3:
            result = list(map(int, sequence))
            if not check_valid(result) or not cvs(sequence):
                return
        for i in list(map(int, sequence)):
            if i > 2 ** 31 - 1:
                return
        for i in range(cons):
            sequence.append(word[:i + 1])
            split_it(word[i + 1:], sequence, cons)
            sequence.pop()
    else:
        result = list(map(int, sequence))
        if check_valid(result) and cvs(sequence):
            fin_result.append(result)


def cvs(sar):
    for i in sar:
        if i != str(int(i)):
            return False
    return True


def check_valid(array):
    for i in range(len(array) - 2):
        if array[i] + array[i + 1] != array[i + 2]:
            return False
    return True


fin_result = []
# test_case = "502113822114324228146342470570616913086148370223967883880490627727810157768164350462659281443027860696206741126485341822692082949177424771869507721046921249291642202139633432706879765292084310"
test_case = "502113822114324228146342470570616913086148370223967883880490627727810157768164350462659281443027860696206741126485341822692082949177424771869507721046921249291642202139633432706879765292084310"

for j in range(1, len(test_case) // 3 + 2):
    split_it(test_case, [], j)
if len(fin_result) == 0:
    print([])
else:
    if len(fin_result[0]) < 3:
        print([])
    else:
        print(fin_result[0])
