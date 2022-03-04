for _ in range(int(input())):
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    blue = a[0] + a[1]
    red = a[-1]
    i, j = 2, n - 2
    while red <= blue:
        if i < j:
            blue += a[i]
            red += a[j]
            i += 1
            j -= 1
        else:
            break

    print(["NO", "YES"][red > blue])