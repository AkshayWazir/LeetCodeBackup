def feedTheAnagrams(words):
    res = {}
    values = []
    answer = []
    for i in words:
        sortedWord = "".join(sorted(list(i)))
        if sortedWord in values:
            answer[res[sortedWord]].append(i)
        else:
            res[sortedWord] = len(values)
            values.append(sortedWord)
            answer.append([i])
    return answer


var = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]

print(feedTheAnagrams(var))
