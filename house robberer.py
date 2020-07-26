def robb(houses):
    if len(houses) <= 3:
        s_eve, s_odd = 0, 0
        for i in range(len(houses)):
            s_eve += houses[i] if i % 2 == 0 else 0
            s_odd += houses[i] if i % 2 != 0 else 0
        return max(s_eve, s_odd)
    else:
        new_arr_mem = [houses[i] if i < 2 else 0 for i in range(len(houses))]
        for i in range(2, len(houses)):
            ans_1 = new_arr_mem[i - 3] if i - 3 >= 0 else 0
            ans_2 = new_arr_mem[i - 2] if i - 2 >= 0 else 0
            new_arr_mem[i] = max(ans_1, ans_2) + houses[i]
    return max(new_arr_mem[len(houses) - 1], new_arr_mem[len(houses) - 2])


print(robb([2, 7, 9, 3, 1, 4, 1, 6, 7]))
