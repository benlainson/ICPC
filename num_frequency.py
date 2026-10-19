#First input is num of inputs
#Values seperated by commas
#Determine which number appears most frequently

def frequencyNum():
    values = [2, 5, 2, 3, 5, 2, 4, 5]
    values.sort()
    curr = 0
    highestFreq = 1
    currFreq = 1
    highestVal = 0

    for value in values:
        if value == curr:
            currFreq += 1
        else:
            curr = value
            currFreq = 1
        if currFreq > highestFreq:
                highestFreq = currFreq
                highestVal = curr
    print("Highest frequencyvalue: ",highestVal)

frequencyNum()