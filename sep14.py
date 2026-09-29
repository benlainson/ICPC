def countVowels():
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    userIn = input("Enter Name: ")
    lowIn = userIn.lower()
    for letter in lowIn:
        if letter in vowels:
            count = count + 1
    print(count)

countVowels()