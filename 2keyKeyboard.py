# A
def get_the_copy(curr, target, prev, steps):
    if curr == target:
        return steps
    elif curr > target:
        return -1
    if prev == 0:
        res = get_the_copy(curr + 1, target, 1, 2)
        return res
    else:
        res = get_the_copy(curr + prev, target, prev, steps + 1)
        res1 = get_the_copy(curr + curr, target, curr, steps + 2)
        if res != -1 and res1 != -1:
            return min(res, res1)
        elif res != -1 and res1 == -1:
            return res
        else:
            return res1


def word_steps(num):
    return get_the_copy(1, num, 0, 0)


print(word_steps(8))
