def busy_hours():
    num = int(input())

    covered = [False] * 24

    for i in range(num):
        start, end = map(int, input().split())

        for hour in range(start, end):
            covered[hour] = True

    total = 0

    for hour in range(24):
        if covered[hour]:
            total += 1

    print(total)

busy_hours()