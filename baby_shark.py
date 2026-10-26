def baby_shark():
    max = 0
    currMax = 1
    max_word = []
    prev = 0
    curr = 1
    words = list(map(str, input().split()))

    for word in words[1:]:
        if words[curr] == words[prev]:
            currMax += 1
            
        else:
            currMax = 1
        prev += 1
        curr += 1
        if currMax > max:
            max = currMax
            max_word.append(word)
        
    print("Max word occurence is: ", max_word[-1])







baby_shark()