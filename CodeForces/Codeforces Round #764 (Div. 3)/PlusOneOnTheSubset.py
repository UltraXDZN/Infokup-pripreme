for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(max(a) - min(a))
