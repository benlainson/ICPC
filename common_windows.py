def commonWindow():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    best = 0
    for i in range(n - k + 1):
        window = nums[i:i + k]
        for x in window:
            curr = window.count(x)
            if curr > best:
                best = curr

    print(best)

commonWindow()