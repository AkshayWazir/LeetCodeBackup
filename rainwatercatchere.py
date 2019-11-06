def get_water(arr):
    if len(arr) == 0:
        return 0
    area = 0
    for i in range(max(arr)):
        temp_height = i + 1
        start = -1
        length = 0
        for j in range(len(arr)):
            if arr[j] >= temp_height and start == -1:
                start = j
            elif start != -1 and arr[j] < temp_height:
                length += 1
            elif start != -1 and arr[j] >= temp_height:
                area += length
                start = j
                length = 0
    return area


def get_water_optimised(height):
    if not height:
        return 0
    max_index = height.index(max(height))
    result = 0
    max_seen = 0
    for i in range(max_index):
        if height[i] >= max_seen:
            max_seen = height[i]
        else:
            result += max_seen - height[i]
    max_seen = 0
    for i in range(len(height) - 1, max_index - 1, -1):
        if height[i] >= max_seen:
            max_seen = height[i]
        else:
            result += max_seen - height[i]
    return result


a = list(map(int, input().split()))
print(get_water_optimised(a))
