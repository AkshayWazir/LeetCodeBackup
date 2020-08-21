def find_solutions(n: int) -> int:
    def check_valid(arr: list) -> bool:
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if (arr[i][1] - arr[j][1]) / (arr[i][0] - arr[j][0]) in [1.0, -1.0]:
                    return False
        return True

    def recur(nums: list, temp: list, row: int):
        if len(temp) == n and check_valid(temp):
            nonlocal count
            count += 1
        elif len(temp) < n:
            for i in range(len(nums)):
                t = nums.pop(i)
                temp.append([row, t])
                recur(nums, temp, row + 1)
                temp.pop()
                nums.insert(i, t)
        else:
            return

    count = 0
    recur([i + 1 for i in range(1, n + 1)], [], 1)
    return count




print(find_solutions(4))
