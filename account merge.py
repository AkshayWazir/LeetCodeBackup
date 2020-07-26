import math


def merge_account(accounts):
    mails, name = dict(), dict()
    for i in range(len(accounts)):
        for j in range(1, len(accounts[i])):
            mails[accounts[i][j]] = min(mails.get(accounts[i][j], math.inf), i)
        name[i] = accounts[i][0]
    for a in range(4):
        for i in range(len(accounts)):
            temp_min = math.inf
            for j in range(1, len(accounts[i])):
                temp_min = min(mails.get(accounts[i][j]), temp_min)
            for j in range(1, len(accounts[i])):
                mails[accounts[i][j]] = temp_min
    res = [[name[i]] + [j[0] for j in mails.items() if j[1] == i] for i in range(len(accounts))]
    i = 0
    while i < len(res):
        if len(res[i]) == 1:
            res.pop(i)
        else:
            res[i][1:] = sorted(res[i][1:])
            i += 1
    return res


temp = [
    ["Hanzo", "Hanzo2@m.co", "Hanzo3@m.co"],
    ["Hanzo", "Hanzo4@m.co", "Hanzo5@m.co"],
    ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co"],
    ["Hanzo", "Hanzo3@m.co", "Hanzo4@m.co"],
    ["Hanzo", "Hanzo7@m.co", "Hanzo8@m.co"],
    ["Hanzo", "Hanzo1@m.co", "Hanzo2@m.co"],
    ["Hanzo", "Hanzo6@m.co", "Hanzo7@m.co"],
    ["Hanzo", "Hanzo5@m.co", "Hanzo6@m.co"]
]
for arr in merge_account(temp):
    for s in range(len(arr)):
        print(arr[s], end=" ")
    print()

