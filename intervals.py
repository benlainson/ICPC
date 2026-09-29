def intervals():
    n, k = map(int, input().split())
    
    diff = [0] * 25  # hours 0-23, with buffer
    
    for i in range(n):
        s, e = map(int, input().split())
        diff[s] += 1
        diff[e] -= 1
    
    result = 0
    current = 0
    for h in range(24):
        current += diff[h]
        if current >= k:
            result += 1
    
    print(result)

intervals()