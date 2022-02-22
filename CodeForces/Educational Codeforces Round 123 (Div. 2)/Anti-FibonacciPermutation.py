for _ in range(int(input())):
    n = int(input())
    l = [i for i in range(1, n+1)][::-1]
    for i in (range(n-1, -1, -1)):
        for j in range(n):
            print(l[j], end=" ")

        if i != 0:
            l[i], l[i-1] = l[i-1], l[i]
        print()
