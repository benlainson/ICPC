def twoSum():
    #6 10
    #2 5 9 8 7 3

    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    seen = {}

    for num in nums:
        complement = k - num
        if complement in seen:
            print(complement, num)
            return
        seen[num] = True
twoSum()