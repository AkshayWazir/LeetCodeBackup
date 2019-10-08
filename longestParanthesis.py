def count(s):
    l_brc, r_brc, m_s = 0, 0, 0
    for i in s:
        if i == "(":
            l_brc += 1
        elif i == ")":
            r_brc += 1
        if r_brc > l_brc:
            r_brc, l_brc = 0, 0
        elif r_brc == l_brc:
            m_s = max(m_s, 2 * r_brc)
    l_brc, r_brc = 0, 0
    for i in range(-1, -1 * len(s) - 1, -1):
        if s[i] == "(":
            l_brc += 1
        elif s[i] == ")":
            r_brc += 1
        if r_brc < l_brc:
            r_brc, l_brc = 0, 0
        elif r_brc == l_brc:
            m_s = max(m_s, 2 * l_brc)
    return m_s


a = input("Enter the Parenthesis : ")
print(count(a))
