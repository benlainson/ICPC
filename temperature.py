def temperature():
    userIn = input("Enter range and temps seperated by value: ")
    numElements = userIn.split("\n")
    nums = numElements.split(",")

    num_max = 0
    num_min = 0

    for num in nums:
        num_int = int(num)
        if num_int > num_max:
            num_max = num_int
        elif num_int < num_min:
            num_min = num_int
    print("Num min: ", (num_min))
    print("Num max: ", (num_max))
    print("Range, ", (num_max - num_min))

temperature()

