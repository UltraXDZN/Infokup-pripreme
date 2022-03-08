for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = []
    for i in range(n, 0, -1):
        index = a.index(i)
        ans += [(index + 1) % i]
        a = a[index + 1:i] + a[:index + 1] + a[i:]

    print(*ans[::-1])
