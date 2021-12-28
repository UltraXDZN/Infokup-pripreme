for _ in range(int(input())):
    n, m, rb, cb, rd, cd = map(int, input().split())
    x, y = 1, 1
    i = 0
    while rb != rd or cb != cd:
        if rb == rd or cb == cd:
            break
        x = [x, -y][rb == n or rb == 0]
        y = [y, -y][cb == m or cb == 0]

        rb, cb = rb + x, cb + y
        i += 1
    print(i)
