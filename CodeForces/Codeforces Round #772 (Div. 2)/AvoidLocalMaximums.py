for _ in range(int(input())):
    ct = 0
    n = int(input())
    a = [int(x) for x in input().split()]

    for i in range(1, n - 1):
        if a[i - 1] < a[i] > a[i + 1]:
            a[i + 1] = a[i] if i + 2 > n - 1 else max(a[i], a[i+2])
            ct += 1

    print(ct)
    print(*a)