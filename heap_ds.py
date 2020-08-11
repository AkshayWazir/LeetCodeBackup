def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_heap(arr, n):
    startIdx = n // 2 - 1
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)


arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
build_heap(arr, len(arr))
