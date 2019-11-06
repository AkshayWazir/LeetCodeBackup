result = []


def get_combinations(tar, res):
    if tar == 0:
        re = list(map(int, res[:len(res) - 1].split(" ")))
        re.sort()
        if re not in result:
            result.append(re)
        return
    elif tar < 0:
        return
    for i in candidates:
        get_combinations(tar - i, res + str(i) + " ")


candidates = list(map(int, input().split()))
target = int(input())
candidates.sort()
get_combinations(target, "")
result.sort()
print(result)
