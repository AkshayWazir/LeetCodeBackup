def search_array(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    temp_arr = [matrix[j][0] for j in range(len(matrix))]
    row_res = binary_search(temp_arr, target)
    if row_res[0] == 1:
        row_res[1] += 1
    col_res = binary_search(matrix[row_res[1] - 1 if row_res[1] - 1 > 0 else 0], target)
    if col_res[0] == -1:
        return False
    else:
        return True


def binary_search(array, target):
    start, end, middle = 0, len(array), len(array) // 2
    while start < end:
        if array[middle] == target:
            return [1, middle]
        elif array[start] == target:
            return [1, start]
        if array[middle] < target:
            start = middle + 1
        elif array[middle] > target:
            end = middle
        middle = (start + end) // 2
    if start >= end:
        return [-1, start]


test4 = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
test1 = [1, 3, 5, 7, 9, 11, 13, 15]
test_cases = [10, 11, 16, 20, 33, 51]
for i in test_cases:
    res = search_array(test4, i)
    if not res:
        print("Failed at : ", i)
print("Completed")

# print("Test 8 : ", search_array(test4, 50))
