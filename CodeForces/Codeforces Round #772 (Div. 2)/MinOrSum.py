for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    ct = 0
    for num in a:
        ct |= num
    print(ct)
