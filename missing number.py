def find_missing(array):
    for i in array:
        array[abs(i)-1] = abs(array[i]) * -1
    missing = []
    for i in range(len(array)):
        if array[i] > 0:
            missing.append(i + 1)
    return missing
