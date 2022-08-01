for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    x = set()
    c = 0
    for num in reversed(a):
        if num in x:
            break
        x.add(num)
        c += 1

    print(n - c)
