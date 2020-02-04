def interval_merger(arr):
    stack = [arr[0]]
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i][0] < stack[len(stack) - 1][0]:
            stack[len(stack) - 1][0] = arr[i][0]
            if arr[i][1] > stack[len(stack) - 1][1]:
                stack[len(stack) - 1][1] = arr[i][1]
        elif arr[i][0] < stack[len(stack) - 1][1] <= arr[i][1]:
            stack[len(stack) - 1][1] = arr[i][1]
        elif arr[i][0] == stack[len(stack) - 1][1]:
            stack[len(stack) - 1][1] = arr[i][1]
        elif stack[len(stack)-1][0] <= arr[i][0] <= stack[len(stack) - 1][1] and stack[len(stack) - 1][0] < arr[i][0] < stack[len(stack) - 1][1]:
            continue
        else:
            stack.append(arr[i])
    return stack


print(interval_merger([[1, 4], [2, 3]]))
