def generate(s):
    def recur(current, temp, cuts):
        if cuts == 3 or len(current) == 0:
            t = current
            if len(t) > 3 or len(t) == 0 or len(str(int(t))) != len(t) or int(t) < 0 or int(t) > 255:
                return
            else:
                temp.append(current)
                result.append(".".join(temp))
        else:
            for i in range(3, 0, -1):
                t = current[:i]
                if 0 <= int(t) <= 255 and len(str(int(t))) == len(t):
                    recur(current[i:], temp + [str(int(t))], cuts + 1)

    result = []
    recur(s, [], 0)
    return result


for i in generate("172162541"):
    print(i)
