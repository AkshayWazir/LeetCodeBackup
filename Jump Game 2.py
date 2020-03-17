def jump_array(arr):
    head, tail = 1, 0
    memory = [0 for j in range(len(arr))]
    for i in range(1, len(arr)):
        if tail + arr[tail] >= head:
            memory[i] = memory[tail] + 1
        else:
            while tail + arr[tail] < head:
                tail += 1
            memory[i] = memory[tail] + 1
        head += 1
    return memory[len(memory) - 1]


print(jump_array([1, 2, 3]))
