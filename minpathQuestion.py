def shortest_path(ai, bi):
    count = 0
    final_list = [(ai[i], bi[i]) for i in range(len(ai))]
    for j in range(len(ai) - 1):
        count += max(abs(final_list[j+1][0] - final_list[j][0]), abs(final_list[j+1][1] - final_list[j][1]))
    return count


coord = []
a = int(input())
for i in range(a):
    point = list(map(int, input().split()))
    coord.append(point)

xi = [coord[i][0] for i in range(len(coord))]
yi = [coord[i][1] for i in range(len(coord))]
print(shortest_path(xi, yi))
