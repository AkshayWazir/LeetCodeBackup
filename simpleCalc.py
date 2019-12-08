def get_exp(word):
    stack = []
    exp = []
    operator = ["-", "+", "*", "/"]
    temp = ""
    for j in word:
        if j.isdigit():
            temp += j
        elif j in operator:
            exp.append(int(temp))
            if len(stack) == 0:
                stack.append(j)


print(eval("1+2*5/3+6/4*2"))
