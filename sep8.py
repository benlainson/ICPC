def missing():
    userIn = "1 2 3 4"
    numList = userIn.split()
    sum = 0
    full = 10
    diff = 0

    for num in numList:
        intNum = int(num)
        sum = sum + intNum
    diff = full - sum
    if diff == 0:
        print("There is no missing number")
    else:
        print("The missing number is", diff)

missing()