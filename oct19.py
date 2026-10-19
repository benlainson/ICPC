def JJ():
    #number has not already been used
    #max number, largest allowed
    #max distance between consecutive moves
    #number of moves
    #10,3,5 - 4,6,9,7,5 = valid
    #10,3,4 - 4,6,10,7
    #invalid
    seen = []
    cap, maxDistance, moves = map(int, input().split())
    nums = list(map(int, input().split()))
    prev = None
    if len(nums) > moves:
        print("Exceeds moves")
        return
    for num in nums:
        if num in seen:
            print("Already used")
            return
        elif num > cap:
            print("Exceeds cap")
            return
        elif prev is not None and abs(prev - num) > maxDistance:
            print("Exceeds max travel distance")
            return
        seen.append(num)
        prev = num
    print("Valid input")


JJ()
