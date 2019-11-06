def get_the_sequence(n):
    if n == 1:
        return "1"
    else:
        start = "1"
        temp = "1"
        temp_count = 0
        for i in range(n):
            temp_word = ""
            for char in range(len(start)):
                if start[char] == temp:
                    temp_count += 1
                else:
                    temp_word += str(temp_count) + temp
                    temp = start[char]
                    temp_count = 1
            temp_word += str(temp_count) + temp
            temp = temp_word[0]
            temp_count = 0
            start = temp_word
    return start


a = int(input())
print(get_the_sequence(a))
