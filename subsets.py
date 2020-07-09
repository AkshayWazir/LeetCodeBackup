def generate_subset(array, temp):
    if len(array) == 0:
        universal_set.append([temp[i] for i in range(len(temp))])
    else:
        generate_subset(array[1:], [i for i in temp])
        temp.append(array[0])
        generate_subset(array[1:], [i for i in temp])


universal_set = []
generate_subset([1, 2, 3], [])
for i in universal_set:
    print(i)
