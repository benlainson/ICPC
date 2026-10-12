def twoSorting():
    #6 10
    #2 5 9 8 7 3

    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    l = 0
    r = len(nums)-1

    while (l < r):
        if nums[l] + nums[r] < k:
            l += 1
        elif nums[l] + nums[r] > k:
            r -= 1
        else:
            print(nums[l], nums[r])
            return
    print("No pairs found")
twoSorting()