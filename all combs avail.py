def generate_combs(n, k, temp, start):
    if k == 0:
        big_array.append([i for i in temp])
    for i in range(start, n + 1):
        generate_combs(n, k - 1, temp + [i], i + 1)


big_array = list()
generate_combs(13, 4, [], 1)
for s in big_array:
    print(s)
