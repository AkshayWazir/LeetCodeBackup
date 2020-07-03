def valid_or_not(arr):
    head, tail = 1, 0
    memory = [0 for j in range(len(arr))]
    if arr[0] > 0:
        for i in range(1, len(arr)):
            if tail + arr[tail] >= head:
                if memory[tail] != 0 or tail == 0:
                    memory[i] = memory[tail] + 1
            else:
                while tail + arr[tail] < head:
                    tail += 1
                if head != tail and tail + arr[tail] >= head:
                    if memory[tail] != 0 or tail == 0:
                        memory[i] = memory[tail] + 1
            head += 1
    print(memory)
    if memory[len(memory) - 1] != 0:
        return True
    else:
        return False


print(valid_or_not([1, 0, 0, 1, 1, 2, 2, 0, 2, 2]))
