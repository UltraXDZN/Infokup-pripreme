for _ in range(int(input())):
    n = int(input())
    l = [int(x) for x in input().split()]
    k = 0
    for i in range(n):
        while l[i] % 2 == 0:
            l[i] //= 2
            k += 1
    print(max(l) * 2 ** k + sum(l) - max(l))
