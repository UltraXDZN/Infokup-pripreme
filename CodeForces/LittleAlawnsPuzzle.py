for _ in range(int(input())):
    x = 1
    n = int(input())
    a = [list(map(int, input().split())) for col in range(2)]
    pairs = [0] * (n + 1)
    for i in range(n):
        pairs[a[0][i]] = a[1][i]

    marked = [False] * (n + 1)

    for i in range(1, n + 1):
        if not marked[i]:
            x *= 2
            x %= 1000000007
            s = [i]
            while True:
                r = s.pop()
                marked[r] = True
                if not marked[pairs[r]]:
                    s.append(pairs[r])
                else:
                    break
    print(x)
