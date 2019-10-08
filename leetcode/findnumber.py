def stringToNum(obj):
    obj = obj.split()
    res = ""
    try:
        for i in obj[0]:
            if ord(i) in range(48, 58) or i == '-' or i == "+":
                if i == "-" and (res[len(res) - 1] == "-" or res[len(res) - 1] == "+"):
                    res = ""
                res += i
            else:
                raise Exception(IndexError)
    except:
        if res == "":
            return 0
        else:
            if res == "":
                return 0
            else:
                res = int(res)
            if res > 2 ** 31:
                return 2 ** 31
            elif res < -2 ** 31:
                return -2 ** 31
            else:
                return res
    if res == "" or res == "-" or res == "+":
        return 0
    else:
        res = int(res)
    if res > 2 ** 31:
        return 2 ** 31
    elif res < -2 ** 31:
        return -2 ** 31
    else:
        return res


a = input()
print(stringToNum(a))
