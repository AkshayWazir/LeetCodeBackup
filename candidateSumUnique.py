result = []


def get_the_combination(index, arr, res, target):
    if target < 0:
        return
    elif target == 0:
        te = list(map(int, res[:len(res) - 1].split(" ")))
        te.sort()
        if te not in result:
            result.append(te)
    elif len(arr) == 1:
        if arr[0] != target:
            result.append([])
            return
        else:
            result.append([arr[0]])
            return
    else:
        for i in range(index + 1, len(arr)):
            get_the_combination(i, arr, res + str(arr[i]) + " ", target - arr[i])


candidates = list(map(int, input().split()))
tar = int(input())
# candidates.sort()
get_the_combination(0, candidates, "", tar)
# result.sort()
print(result)
