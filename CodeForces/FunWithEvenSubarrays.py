for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    i = n - 1
    ct = 0
    while i >= 0:
        if a[i] != a[-1]:
            i -= n - i - 1
            ct += 1
        else:
            i -= 1

    print(ct)