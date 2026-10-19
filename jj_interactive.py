def JJ():
    #number has not already been used
    #max number, largest allowed
    #max distance between consecutive moves
    #number of moves
    #10,3,5 - 4,6,9,7,5 = valid
    #10,3,4 - 4,6,10,7
    #invalid
    seen = []
    cap, maxDistance, moves = 10, 3, 5
    #nums = list(map(int, input().split()))
    iteration = 1
    prev = None
    best = 0
    while True:
        user = int(input("Enter a number(-1 to stop): "))
        if user == -1:
            break

        if iteration > moves:
            print("Exceeds moves")
            seen = []
            iteration = 1
            prev = None
        if user in seen:
            print("Already used")
            seen = []
            iteration = 1
            prev = None
        elif user > cap:
            print("Exceeds cap")
            seen = []
            iteration = 1
            prev = None
            continue
        elif prev is not None and abs(prev - user) > maxDistance:
            print("Exceeds max travel distance")
            seen = []
            iteration = 1
            prev = None
        iteration += 1
        seen.append(user)
        prev = user
        print("Valid input")
        if len(seen) > best:
            best = len(seen)

    print("Longest valid run:", best)


JJ()
