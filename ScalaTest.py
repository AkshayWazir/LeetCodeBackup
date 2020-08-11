def search(A, B):
    res = []
    for i, ch in enumerate(A):
        if ch == "1":
            res.append(i + 1)
    final = []
    for lm, rm in B:
        tl, tr = -1, -1
        for k in res:
            if k >= lm:
                tl = k
                break
        rt = res[::-1]
        for k in rt:
            if k <= rm:
                tr = k
                break
        final.append(tr - tl - 1 if tl != -1 and tr != -1 and tr - tl - 1 >= 0 else 0)
    return final


print(search("0100010010", [[1, 8], [3, 7]]))
