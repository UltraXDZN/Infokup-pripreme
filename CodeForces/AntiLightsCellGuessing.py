for i in range(int(input())):
    n, m = map(int, input().split())
    if n == 1 and m == 1:
        print(0)
    else:
        print([1, 2][min(n, m) != 1])

