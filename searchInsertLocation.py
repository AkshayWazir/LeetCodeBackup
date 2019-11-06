def search_number(array, number):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > number:
            end = mid - 1
        elif array[mid] < number:
            start = mid + 1
        else:
            return mid
    if start == len(array):
        return start
    elif end == -1:
        return 0
    else:
        return start


arr = list(map(int, input().split()))
num = int(input())
print(search_number(arr, num))
