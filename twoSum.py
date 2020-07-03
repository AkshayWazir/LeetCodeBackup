def two_sum_find(box, target):
    for i in range(len(box)):
        temp = box[i + 1:]
        if target - box[i] in temp:
            return [i, i + 1 + temp.index(target - box[i])]
    return []


def two_sum_dict_approach(box, target):
    res = {}
    for i in range(len(box)):
        try:
            temp = res[str(box[i])]
            temp.append(i)
            res[str(box[i])] = temp
        except:
            res[str(box[i])] = [i]

    for i in range(len(box)):
        try:
            found = res[str(target - box[i])]

            if len(found) >= 2:
                return [i, found[1]]
            elif found[0] == i:
                continue
            else:
                return [i, found[0]]
        except:
            continue


print(two_sum_dict_approach([3, 2, 4], 6))
